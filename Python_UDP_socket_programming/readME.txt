						Data Communications -  I
					        Programming Assignment 1
Name : Harshal Shah
ITP-NE, Fall 2016
Date - 09/22/2016

Objective : Transferring content and messages between a	Client and a Server using Sockets.

Note : 	    This program was written using Python v3.5
            It is recommended to run this program on Windows 10 command prompt.
	    It is also recommended that you opne this readME.txt file in notepad.
How to save the program :
	1.Unzip the zip/tar.gz file.
	2.Save the client.py file in a new directory called Client(say)
	3.Save the server.py file in a new directory called Server.
	4.Save the 4 files, viz. Foo1.txt, Foo2.jpg, Foo3.mp3 and Foo4.jpg in the Client Directory where the client program file resides.
	

Note:   1.Foo3 is selected as a large jpeg file.
	2.Foo4 is selected as a large mp3 file, separately along with foo3.jpg for the extra credit.
	3.The server always send an ACK message to the client about the packet number received, if the packet is received out of order, it will print
	  an error mseeage and transmission will stop.
	4.MAX_BUFFER_SIZE variable is defined. It is the maximum size of information that can be exchanged at any particular time.
	  If the packet sixe is smaller than the MAX_BUFFER_SIZE it will send it as if is. If the message/file size is bigger
 	  than MAX_BUFFER_SIZE, it will break the file into small chunks of MAX_BUFFER_SIZE and send it to the client/server.
	5.Operations are explained in comments, in both, client and server program codes.

Some Q&As :
 	1.What do the client.py and server.py do?
	Ans- i)The client prompts the user to enter one of the following commands:
		a) get <filename.extension> (server should send the requested file( by the client) from its directory yo the client, if it does not exist in the server's directory, it should send an error msg to the client.
		b) put <filename.extension> (clinet should put the client's file in the server directory, and print error if the file does not exit in the client's directory)
		c) list (server should send a list of all files in its directory to be displayed by the client on its screen)
		d) exit (refer exlanation below)
	     ii)The client will first send this command to the server and than, depending upon the command entered, both the client and server will execute the required task.
	     iii)If the exit command is used, the server should closed the socket and exit gracefully and the client should again prompt the user for a command and again the client and server should execute these commands
	     commands once the server connection is re established via its socket ( this is done by re executing the server program)
	
	2.How do you run your client and server? 
	Ans- We run the client and the server programs on two separate windows command prompt by the following commands: 
		a)-- <python (3.5) interpreter PATH> <client file path/client.py> <127.0.0.1> <8000>
		b)-- <python (3.5) interpreter PATH> <server file path/server.py> <8000> 
	3.What language/os does your program need to run?
	Ans- The codes are executable in pyhton 3.5 language and windows envrionment. Also, it is recommended to open the client and server code files in IDLE (3.5.2)
	4.Do you have arguments for your programs and what are they?
		i). client arguments are <client.py> <127.0.0.1> <8000>
		ii). server arguments are <server.py> <8000>
		iii). Please enter the appropriate filenames with correct extensions along with get/put commands
		   -- Foo1.txt/ Foo2.jpg/ Foo3.mp3/ Foo4.jpg



