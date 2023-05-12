import grpc
import lab2_pb2_grpc as lab2_pb2_grpc
import lab2_pb2 as lab2_pb2

import hashlib
from string import printable
from itertools import product, count
import pika

def position(moves, map, fileNum, mcounter, layout, channel):
    ans = [0,0]
    facing = 1 # 0 = forward, 2 = backward, 1 = down, 3 = up
    tmp_layout = layout
    tmp_map = map
    tmp_layout[0][0] = 1
    for i in range(len(moves)):
        if(tmp_map[ans[0]][ans[1]] != 0 ):
            #Blow up condition
            #Defuse Bomb
            encoding = 'ascii'
            channel = grpc.insecure_channel('localhost:50051')
            stub_serial = lab2_pb2_grpc.SerialNumberStub(channel)
            tmp = stub_serial.GetSerialNum(lab2_pb2.SerialNumReq(SerNumRequest=tmp_map[ans[0]][ans[1]]))
            serial_num = tmp.SerNumReply
            
            connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
            channel = connection.channel()

            channel.queue_declare(queue='Demine-Queue')

            channel.basic_publish(exchange='',
                      routing_key='Demine-Queue',
                      body=f'Position: {ans[0]}, {ans[1]} id: {fileNum} serial: {serial_num} ')
            print(" [x] Sent 'Hello World!'")
            
            #cracked = crack(encoding, str(serial_num))
            
            

            connection.close()
            tmp_map[ans[0]][ans[1]] = 0
                
        else:
            if(moves[i] == "L"):
                facing = facing - 1 if facing - 1 >= 0 else 3
            elif(moves[i] == "R"):
                facing = facing + 1 if facing+1 <=3 else 0
            elif(moves[i] == "M"):
                mcounter += 1
                #Move forward
                if(facing == 0 and ans[1] + 1 < len(map[0])):
                    ans[1] += 1
                    tmp_layout[ans[0]][ans[1]] = 1
                #Move Back
                elif(facing == 2 and ans[1]-1>0):
                    ans[1]-=1
                    tmp_layout[ans[0]][ans[1]] = 1
                elif(facing == 1 and ans[0] + 1 < len(map)):
                    
                    ans[0] += 1
                    tmp_layout[ans[0]][ans[1]] = 1
                elif(facing == 3 and ans[0] > 0):
                    ans[0] += -1
                    tmp_layout[ans[0]][ans[1]] = 1
    
    tmp_layout[ans[0]][ans[1]] = 2 #This indicates the  finishing position            
    # draw(tmp_layout, fileNum, channel)
    return ans




def run():
    print("hello")
    #Get Map
    channel = grpc.insecure_channel('localhost:50051')
    def getMeMap():
        
        stub = lab2_pb2_grpc.BombStub(channel)
        tmp = stub.GetMap(lab2_pb2.GetMapRequest(MapReq="Get Map"))
        temp = tmp.values.split()
        
        cols = int(temp[0])
        rows = int(temp[1])
        maps2 = [[0]*cols for i in range(rows)]

        for i in range(2, len(temp)):
            
            row = int((i - 2)/rows)
            col = (i-2) - row*rows
            if(temp[i] != '0'):
                maps2[row][col] = temp[i]
        print(maps2)
        return cols, rows, maps2
    
    #Get Rover Moves
    stub_move = lab2_pb2_grpc.RoverMovesStub(channel)
    print("\n")
    i = "null"
    
    while(i != "exit"):
        print("Enter exit to exit the prog")
        i = input('Please enter rover Number \n')
        i = int(i)
        cols, rows, maps2 = getMeMap()
        if(i <= 10):
            moves = stub_move.GetMoves(lab2_pb2.GetRoverMoves(reoverReq=f"{i}"))
            layout = [[0]*cols for i in range(rows)]
            mcounter = 0
            ans = position(moves.RoverStream, maps2, i, mcounter, layout, channel)
            print(ans)
        else:
            print("Etner a Number between 1-10 \n\n")

    
    
run()