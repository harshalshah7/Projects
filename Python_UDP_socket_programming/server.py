import socket
import sys
import os

def get(msg,serversocket, clientAddr):
    if doesFileExist(cmds[1]):                                                          #go to doesfileexit() to check if the file exists
        sendData(serversocket,"FILEEXISTS", clientAddr)                                 #will notify client via senddata() that file exists
        msgToSend = readFile(cmds[1])                                                   #file content saved in msg is saved in msgToSend to send to server
                
        expected_curr_packet_num = 0
        for i in range(0,len(msgToSend),MAX_BUFFER_SIZE):                               #for 0 to full size of file,in steps of maxbuffersize
            max_index = min(i+MAX_BUFFER_SIZE, len(msgToSend))                          #define max_index and send only that much size of data
            print("Sending from ", i, " to ", max_index)
            sendData(serversocket, msgToSend[i:max_index],clientAddr)                   #send data specifically for a particular chunck of a file 
            msg,clientAddr = serversocket.recvfrom(MAX_BUFFER_SIZE)                     #expect to get an ack stating the packet number it obtained
            if msg != ("PACKET"+str(expected_curr_packet_num)).encode():                #if its not equal to the packet number that was expected, print an error
                print("error got "+ msg)
            else:
                print("PACKET"+str(expected_curr_packet_num) + " sent")                 # if you get ack stating that the expected packet was received by client, print correctly received
                expected_curr_packet_num +=1;                                           #increase to send next expected msg
        sendData(serversocket,"FILEEND",clientAddr)                                     #once it has succesfully send the entire file, it will come outta for loop and send fileend to notify the client that the entire file was send
        print ("File sent")
    else:                                                                               #if file doesnt exist we notify the client
        msgToSend = "File doesnot exist"
        sendData(serversocket,msgToSend,clientAddr)
def put(msg,serversocket,clientAddr):
    print('putting ', cmds[1]) 
    serversocket.sendto("Please start sending the file".encode(), clientAddr)   
    fp = open(cmds[1], 'wb')                                                            #create a new file in server directory in binary write mode
    tot_length_obtained = 0                                                             #to check how much data is received at any point of time
    curr_packet_num = 0                                                                 #to inform the client about which pakcet it should be receiving 
    while True:
        data,clientAddr = serversocket.recvfrom(MAX_BUFFER_SIZE)                        #receive the file
        lengthdata = len(data)                                                          #to check the size of the pakcet that is received
        tot_length_obtained = tot_length_obtained + lengthdata
        if data == "FILEEND".encode():                                                  #if client sends a "FILEEND" than closde the new file and break the while and send ACK to client that the file was received
            break
        print("got this far ", tot_length_obtained)                                     #print the size of data that is received till now
        sendData(serversocket, "PACKET"+str(curr_packet_num), clientAddr)               #To inform the client about the current packet number that  was received
        curr_packet_num += 1;  
        fp.write(data)                                                                  #append data to the new file till the "FILEEND" doesnt arrive
    fp.close()          
    print("File obtained")
def list(msg, serversocket,clientAddr):
    print('listing files')
    msgToSend = listFiles()                                                             #Go to listFiles() function to send a list of all the files in the server directory
    print(msgToSend)
    serversocket.sendto(msgToSend.encode(), clientAddr)                                 #send the list of all files to the client
def exit(msg,serversocket,clientAddr):
    print("Client has informed the server to exit gracefully. Server exiting. Goodbye")             
    serversocket.close()                                                                #close the socket connection           
    sys.exit()                                                                          #exit gracefully
def listFiles():
    list = ""
    for i in (os.listdir(".")) :
        if i != sys.argv[0] :
            list = i + "\n" + list
    return list
    
                                                                                        #tuple into a single string of all files in the directory

def readFile( filename ):
    fp = open(filename, 'rb')                                                           #open the file in binary mode
    msg = fp.read()                                                                     #read the entire file and save in msg
    fp.close()                                                                          #clsoe file
    return msg                                                                          #return file 

def doesFileExist( filename ):                                                          #will cheeck if the file exists or not
    return os.path.isfile(filename)

def sendData(s, msg, clientAddr):
    try :
        if isinstance(msg, bytes):                                                      #if its already in bytes, do not encode
            serversocket.sendto(msg, clientAddr)
        else:                                                                           #in all other cases encode
            serversocket.sendto(msg.encode(), clientAddr)
    except serversocket.error as msg:
        print('Error Code : ' + str(msg[0]) + ' Message ' + msg[1])   
    
def saveFile (filename, msg):
    fp = open('recieved_'+filename, 'wb')
    fp.write(msg)
    fp.close()

MAX_BUFFER_SIZE = 8*1024                                                                #max size of any packet being passed btw SC.
'''reject port no less than 5000'''
if len(sys.argv) == 2:                                                                  #check exactly 2 args are provided
    try:
        port = int(sys.argv[1])
        print ('Binding to ', port)
    except ValueError as e:
        print('Arguments to program are server.py <port>,\nEnter Correct inputs')
        sys.exit()
else:                                                                                   #print an error prompting user to provide input in proper format
    print('Arguments to program are server.py <port>')
    sys.exit()
if port <= 5000:
    print("Its less the 5000")
    sys.exit()


try:
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)                     #creating server socket
    serversocket.bind(('', port))                                                       #binding the new socket to all ips*
    print("waiting on port:", port)
except socket.error:
    print('Failed to create socket')
    sys.exit()
    
while 1:                                                                                #keep waiting fr an input from client
    
        msg, clientAddr = serversocket.recvfrom(MAX_BUFFER_SIZE)                        #we receive command from client
        msg = msg.decode()
        cmds = msg.strip().split(' ')    

        if cmds[0].lower() == 'get':            
            get(msg, serversocket,clientAddr)                                           #go to get function
        elif cmds[0].lower() == 'put':
            put(msg, serversocket,clientAddr)                                           #go to put function
        elif cmds[0].lower() == 'list':                                     
            list(msg,serversocket,clientAddr)                                           #go to list function
        elif cmds[0].lower() == 'exit':         
            exit(msg,serversocket,clientAddr)                                           #go to exit function
        else:                                                                           #if the user on client side inputs an invalid command
            msgToSend = 'unknown command'
            serversocket.sendto(msgToSend.encode(), clientAddr)        
        
            
    
