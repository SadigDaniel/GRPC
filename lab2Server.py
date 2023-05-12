#!/usr/bin/env python
from concurrent import futures
import grpc
import lab2_pb2_grpc 
import lab2_pb2 
import threading
import requests
import json


import pika, sys, os

def get_data(api):
        response = requests.get(f"{api}")
        if response.status_code == 200:
            return(response.json())
        else:
            print(f"Hello person, there's a {response.status_code} error with your request")
            return "Nothing"


class BombServicer(lab2_pb2_grpc.BombServicer):
    def GetMap(self, request, context):
        f = open("maps.txt", "r")
        temp = f.read()
        print(temp)
        print("HIIIIII")
        return lab2_pb2.GetMapReply(values=temp)

class RoverMovesServicer(lab2_pb2_grpc.RoverMovesServicer):
    def GetMoves(self, request, context):
        tmp = get_data(f"https://coe892.reev.dev/lab1/rover/{request.reoverReq}")
        rover_moves = (tmp['data']['moves'])
        return lab2_pb2.ReturnRoverMoves(RoverStream=rover_moves)
    
class SerialNumberServicer(lab2_pb2_grpc.SerialNumberServicer):
    def GetSerialNum(self, request, context):
        f = open("serialNumFile.txt", "r")
        temp = f.read().split()
        index = int(request.SerNumRequest)
        if(index > len(temp)):
            index = 1
        ret_val = temp[int(request.SerNumRequest)]
        print(ret_val)
        return lab2_pb2.SerialNumReply(SerNumReply=int(ret_val))


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))  # Create a thread pool with 10 worker threads
    lab2_pb2_grpc.add_BombServicer_to_server(BombServicer(), server)
    lab2_pb2_grpc.add_RoverMovesServicer_to_server(RoverMovesServicer(), server)
    lab2_pb2_grpc.add_SerialNumberServicer_to_server(SerialNumberServicer(), server)
 
    
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started listening on port 50051...")
    server.wait_for_termination()



def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='Defused-Mines')

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)

    channel.basic_consume(queue='Defused-Mines', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        
        t1 = threading.Thread( target=main, args=()) 
        t2 = threading.Thread( target=serve, args=()) 
        
        t1.start()
        t2.start()
        
        t1.join()
        t2.join()
      
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
            t1.join()
            t2.join()