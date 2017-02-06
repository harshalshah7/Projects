##################################################################################################################
# Copyrights 2016 Harshal Shah All Rights Reserved
# The information contained herein is property of the Authors.
# The copying and distribution of the files is prohibited except by express written agreement with the Authors.
# Authors: Harshal Shah
#Date: Aug 2016
##################################################################################################################
import socket
import sys
from time import sleep
import time
import threading

def multiple(msg, client, a,l):
    data=client.recv(4096)
    data=data.decode()
    print(data)
    m=time.time()
    print("Thread for handling handling multiple files: {}\nStart time: {}\nEnd time: {}\nTime taken to handle the request: {}".format(a, l ,m,(m-l)))
    return(0)

def single(msg, client, b, x):
    data=client.recv(4096)
    data=data.decode()
    print(data)
    y=time.time()
    print("Thread for handling handling single file: {}\nStart time: {}\nEnd time: {}\nTime taken to handle the request: {}".format(b, x ,y,(y-x)))
    return(0)

'''main program starts here'''
host='127.0.0.1'
port=8000
backlog=5
threadlist=[]
try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    client.connect((host,port))  
except socket.error():    
    print("not possible to listen")
    sys.exit()
a=0
for i in range (0,100):
    a = a+1
    msg= "GET " + "/index" + str(i+1) + ".html HTTP/1.1\r\nHost: localhost:8000\r\nConnection: keep-alive\r\nPragma: no-cache\r\nCache-Control: no-cache\r\nUpgrade-Insecure-Requests: 1\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)\r\nAppleWebKit/537.36 (KHTML, like Gecko)\r\nChrome/53.0.2785.143\r\nSafari/537.36\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8\r\nAccept-Encoding: gzip, deflate, sdch\r\nAccept-Language: en-US,en;q=0.8"
    msg=msg.encode()
    try:
        client.send(msg)
        print(client)
        l=time.time()
        cs=threading.Thread(target=multiple,args=(msg, client, a, l))
        cs.start()                                                              #start thread   
        threadlist.append(cs)                                                  #print threads
        print(len(threadlist)) 
        print("Active ", threading.active_count())
        sleep(0.01)
    except Exception as e:
        print(e)
        print("sorry")
b=0            
for i in range(0,100): 
    b=b+1
    msg= "GET / HTTP/1.1\r\nHost: localhost:8000\r\nConnection: keep-alive\r\nPragma: no-cache\r\nCache-Control: no-cache\r\nUpgrade-Insecure-Requests: 1\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)\r\nAppleWebKit/537.36 (KHTML, like Gecko)\r\nChrome/53.0.2785.143\r\nSafari/537.36\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8\r\nAccept-Encoding: gzip, deflate, sdch\r\nAccept-Language: en-US,en;q=0.8"
    msg=msg.encode()
    try:
        client.send(msg)
        print(client)
        x=time.time()
        cs=threading.Thread(target=single,args=(msg, client,b, x))
        cs.start()                                                              #start thread
        threadlist.append(cs)                                                       #print threads
        print(len(threadlist)) 
        print("Active ", threading.active_count())
        sleep(0.01)
    except Exception as e:
        print(e)
        print("sorry")    
sys.exit()
