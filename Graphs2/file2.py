#author: Harshal Shah Harshal.Shah@colorado.edu
#name: file2.py
#purpose: Create a two line graph with data from pinging two hosts
#date: 11/06/2016
#version: 9.2
try:
    import sys
    import os
    import matplotlib.pyplot as plt 
    import requests
    import csv
    from prettytable import PrettyTable
    import subprocess
except:
    print("Some modules couldnt be installed properly")
    sys.exit()
xyz=[]
abc=[]
def Checkargs1():
    if (len(sys.argv) != 1):
        if (len(sys.argv) != 2):
            print("Please provide proper arguments:\nUsage:<filename.py> <output_filename/optional>")
            sys.exit()
def Checkargs():
    if (len(sys.argv)== 2):
        return(1)
    else: 
        
        return(0)
           
Checkargs1()        
for i in range (0,50):
    try:
        response=subprocess.check_output(["ping", "8.8.8.8"], stderr=subprocess.STDOUT, universal_newlines=True)
    except:
        print("Check your internet connection")
        sys.exit()
    print(response)
    a=response.split(":")
    b=a[8].split("=")
    c=b[3].split("ms")
    print(c[0])
    xyz.append(c[0])
    
for i in range (0,50):
    try:
        response1=subprocess.check_output(["ping", "4.2.2.1"], stderr=subprocess.STDOUT, universal_newlines=True)
    except:
        print("Check your internet Connection")
        sys.exit()
    print(response1)
    d=response1.split(":")
    e=d[8].split("=")
    f=e[3].split("ms")
    print(f[0])
    abc.append(f[0])
print(xyz)
print(abc) 
table = PrettyTable()
table.add_column("8.8.8.8" , xyz)
table.add_column("4.2.2.1" , abc)
print(table)
aaa=Checkargs()
if aaa== 1:
    if os.path.isfile(sys.argv[1]):
        print("Choose a different filename, The file already exists")
        
    elif ((".txt" in sys.argv[1]) or (".csv" in sys.argv[1])):
        f=open(sys.argv[1], "w")
        f.write(str(table))
        f.close()    
    else:
        print("Please provide a valid filename, if you wish to save the file in proper format\nUsage:<filename.txt/filename.csv>")
else :
    print("You did not ask for saving the file")    
plt.xlabel("X label")
plt.ylabel("Y Label")
plt.title("This is Title")
plt.plot(xyz)
plt.plot(abc)   
plt.legend(['Line 1', 'Line 2'], loc='upper left')
plt.xticks(range(50), range(50), rotation="vertical")
plt.savefig("filename1.png")
plt.show()
 
sys.exit()