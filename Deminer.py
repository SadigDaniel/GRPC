#!/usr/bin/env python
import pika, sys, os
import threading

import hashlib
from string import printable
from itertools import product, count
#Send
def send(response):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='Defused-Mines')

    channel.basic_publish(exchange='',
                        routing_key='Defused-Mines',
                        body=f'from 1: {response}')
    print(" [x] Sent from deminer 1")

    connection.close()

def send2(response):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='Defused-Mines')

    channel.basic_publish(exchange='',
                        routing_key='Defused-Mines',
                        body=f'From deminer 2: {response}')
    print(" [x] Sent From deminer 2'")

    connection.close()
#Receive

def crack1(encoding, serial_Num):
        print(encoding)
    
        def passwords(encoding):
            chars = [c.encode(encoding) for c in printable]
            for length in count(start=1):
                for pwd in product(chars, repeat=length):
                    yield b''.join(pwd)
                
        for pwd in passwords(encoding):
            input_string = serial_Num.encode(encoding) + pwd
            hash_result = hashlib.sha256(input_string).hexdigest()
            if hash_result.startswith("0"*6):
                print(hash_result)
                print(pwd.decode(encoding))
                return pwd.decode(encoding)
def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    
    queue = channel.queue_declare(queue='Demine-Queue')
    
    def callback(ch, method, body):
        response = body.split()[-1]
        encoding = 'ascii'
        print(f' \n {body} and {response} \n')
        ans = crack1(encoding, str(response))
        send(ans)
        print(f" [x] Received {body}")
       

    channel, method, body = channel.basic_get(queue='Demine-Queue', auto_ack=True)
    print(f' \n There are {queue.method.message_count} messages in the queue \n')
    if(queue.method.message_count == 0):
        print("empty ")
        return "Error"
    callback(channel, method, body)
    #channel.start_consuming()
    
    print(' [*] Waiting for messages. To exit press CTRL+C')
    #channel.start_consuming()

def main2():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    
    queue = channel.queue_declare(queue='Demine-Queue')
    
    def callback(ch, method, body):
        response = body.split()[-1]
        encoding = 'ascii'
        ans = crack1(encoding, str(response))
        send2(ans)
        print(f" [x] Received {body}")

    channel, method, body = channel.basic_get(queue='Demine-Queue', auto_ack=True)
    print(f' \n There are {queue.method.message_count} messages in the queue \n')
    if(queue.method.message_count == 0):
        print("empty ")
        return "Error"
    callback(channel, method, body)
    

print("Hello we have 2 deminers please select wich one you want to run ! \n")
imp = input("Enter 1 for Deminer 1 and 2 for 2")
t1 = threading.Thread( target=main, args=()) 
t2 = threading.Thread( target=main2, args=()) 
while(imp != -1):
    if(int(imp) == 1):
        if(t1.is_alive() == False):
            t1.start()
        else:
            print(t1.is_alive())
            print("t1 is busy please wait")
        
    else:
        
        t2.start()
    imp = int(input("enter 1 or 2 again"))
    
t1.join()
t2.join()


t1 = threading.Thread( target=main, args=()) 
t2 = threading.Thread( target=main2, args=()) 
while(imp != -1):
    if(int(imp) == 1):
        if(t1.is_alive() == False):
            t1.start()
        else:
            print(t1.is_alive())
            print("t1 is busy please wait")
        
    else:
        
        t2.start()
    imp = int(input("enter 1 or 2 again"))
    
t1.join()
t2.join()
    
    
