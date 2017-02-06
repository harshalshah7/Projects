################################################################################################################
# Copyrights 2016 Harshal Shah All Rights Reserved
# The information contained herein is property of the Authors.
# The copying and distribution of the files is prohibited except by express written agreement with the Authors.
# Authors: Harshal Shah
#Date: Sept 2016
################################################################################################################
#!/usr/bin/env python 
import socket
import threading
import sys
import os
import time
def shutit():
    while 1:
        try:
            input()
        except Exception:
            os._exit(1)

def thred(client, address, timer):
    while True:                                                   #receive request
        try :                                                                                       
            data = client.recv(4096).decode()                                               
            if data:
                client.settimeout(int(timer))                                                   #set timeout to handle persistent connection request                                                          
            data=data.split()
            if ((data[2] == 'HTTP/0.9')):
                fh=open(root+'501Error.html', 'rb')
                msg=fh.read()
                heads=data[2]+ " 501 Not Implemented: Version\nContent-Type: text/html\n\n"
                #heads=heads.encode()
                client.send(heads.encode()+msg)
                client.close()
                break           
            if data[0] == 'GET':
                lmn=0
                mmm=0
                for i in data:                                                                  #to implement a request buffer for pipelining requests
                    lmn=lmn+1
                    mmm=mmm+1
                    if i == 'GET':
                        abc=lmn-1                        
                        x=get(client, data, root, abc)
                        if x==0:    
                            break
                        else:
                            continue
                if mmm != len(data):
                    break
                else:
                    continue
            else:
                fh=open(root+'501Error.html', 'rb')
                msg=fh.read()
                heads=data[2]+ " 501 Not Implemented: Method\nContent-Type: text/html\n\n"
                #heads=heads.encode()
                client.send(heads.encode()+msg)
                client.close()
                break
        except Exception as e:
            print(e)
            print("Closing Client connection")
            client.close()
            break
                        
def GimmeContent(m):                                                    #will send back the format of the file
    x=ext_format[m]
    return(x)
    
def SendFile(file_and_exts,root,client, msn, x, data):                  #to send the requested file contents
    fh=open(msn, 'rb')
    msg=fh.read()
    test = root + file_and_exts
    size = os.stat(test).st_size
    fh.close()
    if 'keep-alive' in data:
        heads= data[2]+ " 200 OK\nContent-type: " + x + "\nContent-Length:" + str(size) + "\n" + "Connection: Keep-Alive\n\n"
        client.send(heads.encode('utf-8')+msg)
        client.send(msg)
        return(1)
    else:    
        heads= data[2]+ " 200 OK\nContent-type: " + x + "\nContent-Length:" + str(size) + "\n" + "Connection: Close\n\n"
        client.send(heads.encode('utf-8'))
        client.send(msg)
        client.close()
        return(0)
      
def get(client, data, root, abc):                                               #to send the default page to the browser
    if ((data[abc+1] == '/') or (data[abc+1] == '/Document_Root_Directory/')or (data[abc+1] == '/Document_Root_Directory') or (data[abc+1] == '/index.htm') or (data[abc+1] =='/root/index.htm') or (data[abc+1] =='/index.html') or (data[abc+1] =='/index.ws') or (data[abc+1] =='./root/index.html')) :
        fh=open(root1, 'rb')
        msg=fh.read()
        test = root1
        size = os.stat(test).st_size
        fh.close()
        if 'keep-alive' in data:
            heads=data[2] + " 200 OK\nContent-type: text/html\nContent-Length:" + str(size) + "\n" + "Connection: Keep-Alive\n\n"
            client.send(heads.encode('utf-8'))
            client.send(msg)
            return(1)    
        else:
            heads=data[2] + "200 OK\nContent-type: text/html\nContent-Length:" + str(size) + "\n" + "Connection: Close\n\n" #this will be removed
            #client.send(heads.encode('utf-8'))
            client.send(heads.encode()+msg)
            client.close()
            print("Closing client connection")
            return(0)
    else :                                                                          #to handle any otehr request and also to check for error handling
        try:
            if (("$" in data[abc+1]) or ("%" in data[abc+1]) or ("*" in data[abc+1]) or (":" in data[abc+1])):
                fh=open(root+'400Error.html', 'rb')
                msg=fh.read()
                heads=data[2] + " 400 Bad Request\nContent-Type: text/html\n\n"
                client.send(heads.encode()+msg)
                client.close()
                return(0)
            if (("/" not in data[abc+1]) or ("//" in data[abc+1])):
                fh=open(root+'400Error.html', 'rb')
                msg=fh.read()
                heads=data[2]+ " 400 Bad Request\nContent-Type: text/html\n\n"
                client.send(heads.encode()+msg)
                client.close()
                return(0)
            fil=data[abc+1].split('/')
            n=int(len(fil))
            if "." in fil[n-1]:
                file_and_ext=fil[n-1].split('.')
                file_and_exts=file_and_ext[0]+ "." + file_and_ext[1]
                file_ext=file_and_ext[1].lower()
                if os.path.isfile("./Document_Root_Directory/"+ file_and_exts):             #check if the requested file exists
                    if ("."+file_ext in list_of_ext) :                                      #check if the requested file format is supported by the server
                        l=0
                        for i in list_of_ext:
                            l=l+1
                            if i == "."+file_ext:
                                m=l-1
                                x=GimmeContent(m) 
                        msn=root+file_and_exts
                        o=SendFile(file_and_exts,root,client, msn, x, data)
                        if o==0:
                            return(0) 
                    else:   
                        fh=open(root+'501Error.html', 'rb')
                        msg=fh.read()
                        heads=data[2] + " 501 Not Implemented: File not Supported\nContent-Type: text/html\n\n"
                        client.send(heads.encode()+msg)
                        client.close()
                        return(0) 
                else:
                    fh=open(root+'404Error.html', 'rb')
                    msg=fh.read()
                    heads=data[2] + " 404 Not Found Requested URL does not exist\nContent-Type: text/html\n\n"
                    client.send(heads.encode()+msg)
                    client.close()
                    return(0)
            else:
                fh=open(root+'400Error.html', 'rb')
                msg=fh.read()
                heads=data[2] + " 400 Bad Request: Invalid URL\nConten-Type: text/html\n\n"
                client.send(heads.encode()+msg)
                client.close()
                return(0)    
        except :
            fh=open(root+'500Error.html', 'rb')
            msg=fh.read()
            heads=data[2] + " 500 Internal Server Error\nContent-Type: text/html\n\n"
            client.send(heads.encode()+msg)
            client.close()
            return(0)
        return(1)  

'''main prog starts here'''

try: 
    fl=open('./Document_Root_Directory/ws.conf')
except:
    print("Cannot find the configuration file")
    sys.exit()
x=0
file_types=[]
list_of_ext=[]
ext_format=[]
for line in fl:                                                                             #to read the configuration file
    x=x+1
    if x == 2:
        mas=line.split()
        port=int(mas[1])
        print("Connected on port number: " ,port)                                                  #for using ephemeral port numbers only
        if ((int(port)<= 1024) or ( int(port)>65535)):
            print("Sorry, please enter port number greater than 1024, but less than 65536")
            sys.exit()       
    if line.startswith("DocumentRoot"):                                                         #document root directory
        roo = line.split()  
        root = roo[1]
    if line.startswith("DirectoryIndex"):                                                           #default page
        roo1 = line.split()
        root1 = roo1[1] 
    if line.startswith("ContentType"):
        file_types=line.split()
        list_of_ext.append(file_types[1])
        ext_format.append(file_types[2])
    if line.startswith("KeepAliveTime"):
        timers=line.split()
        timer=timers[1]
host= ''
backlog=5
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((host,port))
    s.listen(backlog)
except socket.error():    
    print("Socket Error")
    sys.exit()
threadlist=[]
while True: 
    try:
        print("Waiting to accept connection")
        threading.Thread(target=shutit).start()
        client, address = s.accept()
        print(client)
        cs=threading.Thread(target=thred,args=(client, address, timer))
        cs.start()                                                              #start thread
        threadlist.append(cs)    
    except (Exception,KeyboardInterrupt, EOFError) :                            #For handling Exceptions
        print("Sorry, an Error Occured")
        sys.exit()
       
