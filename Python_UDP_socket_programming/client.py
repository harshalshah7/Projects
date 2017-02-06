import socket
import sys
import os
def get(msg,host,port,s):
    print('getting ', cmds[1])
    sendCommand(msg, host, port)                                                                    #send 'get fillename' to server via SendCommand() 

    (data, servaddr,lengthdata) = getData(s)                                                        #server will return fileesxits or nt exists msg or server connection termination msg
    if data.decode() == "fx" :
        print("Please wait for the server to re establish its connection")
    else:    
        if data == 'FILEEXISTS'.encode():                                                           #if file exists
            fp = open('recieved_'+cmds[1], 'wb')                                                    #open a new file to write data from the server
            tot_length_obtained = 0
            curr_packet_num = 0
            while True:                                                                             #while will keep receiving and saving data in new file untill it receives 'fileend' msg from server
                data, servaddr = s.recvfrom(MAX_BUFFER_SIZE)
                lengthdata = len(servaddr)                                                          #because its binary len is not working
                tot_length_obtained = tot_length_obtained + lengthdata
                if data == "FILEEND".encode():                                                      #if it receives filend from server it will brk the while loop and save the file
                    break

                print("got this much data so far ", tot_length_obtained)
                sendCommand("PACKET"+str(curr_packet_num), host, port)                              #will send ack to server stating the current packet number received 
                curr_packet_num += 1;                                                               #increament packet number
                fp.write(data)                                                                      #append to the new file
            fp.close()
            print("File obtained")
        else:                                                                                       #if file doesnt exist print data'File does not exist'(Receives from server side)
            print(data)
def put(msg,host,port,s):
    print('putting ', cmds[1])
    if cmds[1]:                                                                                     #do it only if string is not empty
        if doesFileExist(cmds[1]):                                                                  #check if file exists in client directory
            sendCommand(msg, host, port)                                                            #inform the server about the command entered by the user
            data, servAddr,datalen = getData(s)
            if data.decode()== "fx" :
                print("Please wait for the server to re establish its connection")
            else:
                msgToSend = readFile(cmds[1])                                                       #read the file to send to server
                expected_curr_packet_num = 0                                                        #to check whether the right packet was delivered to the excpected packet ws sent properly or not
                for i in range(0,len(msgToSend),MAX_BUFFER_SIZE):
                    max_index = min(i+MAX_BUFFER_SIZE, len(msgToSend))                              #define max_index and send only that much size of data
                    print("Sending from ", i, " to ", max_index)    
                    sendData( msgToSend[i:max_index],host,port)                                     #send only max_index sixe of data as a chunk to the  server
                    msg,clientAddr = s.recvfrom(MAX_BUFFER_SIZE)
                    msg = msg.decode()
                    if msg != ("PACKET"+str(expected_curr_packet_num)):                             #if the sent packet was not received properly at server side, print an error
                        print("error! got ack for ", msg, " instead of ",("PACKET"+str(expected_curr_packet_num)))
                        print(" Please resend your data")
                    else:
                        print("PACKET"+str(expected_curr_packet_num) + " sent")                     #acknowledge that sent packet was received properly
                        expected_curr_packet_num +=1;
                sendData("FILEEND",host,port)                                                       #send this to inform server that the entire file has been sent
                print("file sent")
        else:
            print("File doesnot exist")                                                             #if the file doesnt exist
def list(msg,host,port,s):
    print('listing ')
    sendCommand(msg, host, port)         
    data, servAddr,datalen = getData(s)                                                             #ask server for a list of all the files in its directory, receive the list and display it for the user on client end 
    if data.decode() == "fx":
        print("Please wait for the server to re establish its connection")
    else:    
        print("files are ", data.decode())
def exit(msg,host,port,s):                                                                          #ask the server to exit
    print("Server Exiting")
    sendCommand(msg, host, port)                                                                    
def sendCommand(msg, host, port):                                                                   #function to send the command provided as input by the user
    try :
        
        if isinstance(msg, bytes):                                                                  #if its already in bytes, do not encode
            s.sendto(msg, (host, port))
        else:                                                                                       #in all other cases encode
            s.sendto(msg.encode(), (host, port))
    except socket.error as msg:                                                                     #to handle exception
        print('Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    
def getData(s):                                                                                     #function defined to receive data 
    try :
        try:                                                                                        #if the server connection was terminated
            data, servAddr = s.recvfrom(MAX_BUFFER_SIZE)                                        
        except ConnectionResetError :
            print("server was gracefully closed")
            data="fx".encode()
            servAddr= "fx".encode()
            return(data, servAddr, len(data))                                                       #return a "not important" value to break the loop
             
        if isinstance(data,str):                                                                    #if the received data is a string, decode it
            data = data.decode()
            print('Server reply with data of length ' + str(len(data)))
    
    except socket.error as msg:                                                                     #to handle exception
        print('Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    
    return data, servAddr, len(data)
    
def readFile( filename ):                                                                           #function defined to read a file in binary format
    fp = open(filename, 'rb')
    msg = fp.read()
    fp.close()
    return msg

def doesFileExist( filename ):                                                                      #function defined to check whether the file exits or not
    return os.path.isfile(filename)

def sendData(msg, host, port):                                                                      #to send the command to the server  
    sendCommand(msg, host, port)
   

MAX_BUFFER_SIZE = 8*1024                                                                            #max size of any packet being passed btw client and server.
    
if len(sys.argv) == 3:                                                                              #look for 3 args
    try:
        host = sys.argv[1]
        port = int(sys.argv[2])
        print ('Connecting to ', host, ':', port)
    except ValueError as e:                                                                         #handle error and to print the exact error msg in the error
        print('Arguments to program are client.py <hostip> <port>,\nEnter Correct inputs')
        sys.exit()
else:                                                                                               #if insufficient arguments are provided
    print('Arguments to program are client.py <hostip> <port>')
    sys.exit()

try:                                                                                            
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)                                            #defining a socket
except socket.error:
    print('Failed to create socket')
    sys.exit()



while(1) :
    try:
        msg = input('Enter message to send : ')                                                     #asking for user input
    except (EOFError, KeyboardInterrupt ):
        print("\n closing client,bye")
        sys.exit()
                                                                                                    
    cmds = msg.strip().split(' ')                                                                   #parse the commands, remove '' at the ends and beginning and then split
    print(cmds)                                                                                     #we split the user input into <command> <options,if any>
    if cmds[0].lower() == 'get':
        if len(cmds) == 2:
            get(msg,host,port,s)                                                                    #we go to the get function
        else:
            print ("Error")
            
    elif cmds[0].lower() == 'put':
        if len(cmds) == 2:
            put(msg,host,port,s)                                                                    #go to put function
        else:
            print ("Error")
            
    elif cmds[0].lower() == 'list':
        list (msg,host,port,s)                                                                      #go to list funcgtion
    elif cmds[0].lower() == 'exit':                                                                 
        exit(msg,host,port,s)                                                                       #go to exit function
    else:                                                                                           #if the user provides an invalid command
        print('unknown command')
    

    
