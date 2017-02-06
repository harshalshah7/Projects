###################################################################################################################
# Copyrights 2016 Harshal Shah All Rights Reserved
# The information contained herein is property of the Authors.
# The copying and distribution of the files is prohibited except by express written agreement with the Authors.
# Authors: Harshal Shah
#purpose : Create a GUI with 3 buttons
#date : 11/14/2016
####################################################################################################################
try:
    from tkinter import *
    from bs4 import BeautifulSoup
    import sys
    import os
    from socket import gethostbyname
    import requests
except:
    print("An interal Error occured:Could not import one of the modules, Please re-run the program")
    sys.exit()
def Checkargs():
    if len(sys.argv) != 1:
        print("please provide proper arguments\nUsage: file1.py")
        sys.exit()
def endwindow():
    root.destroy()
    sys.exit()

def readIP(x):
    try:
        ip_name=gethostbyname('www.colorado.edu')                                  #can be provided by a user as well using input()
        xyz= "the Ip address of www.colorado.edu is: " + ip_name + "\n"
        t.insert("1.0", str(xyz)) 
    except:
        xyz="Could not get the requested URL: \nEither your internet is not working or the requested URL does not exist or some other internal error was caused\nPlease re run the program."
        t.insert("1.0", str(xyz))
        sys.exit()
def use_requests():
    try:
        r=requests.get('http://www.colorado.edu')
        rm=r.content
        
        rm=rm.decode()
        rm=rm.split("<title>")
        rm=rm[1].split("</title>")
        mnm= "The title of the www.colorado.edu's homepage is: "+ rm[0] +"\n"
        t.insert("1.0", str(mnm))
    except :
        mnm= "Could not get the requested URL: \nEither your internet is not working or the requested URL does not exist or some other internal error was caused\nPlease re run the program."
        t.insert("1.0", str(mnm))
        sys.exit()
Checkargs()

root=Tk()
window=Label(root,text="www.colorado.edu: Properties")
window.pack()
root.geometry('480x480')
t=Text()
t.pack()

buttonA=Button(root,text="Button A", command=lambda: readIP("A"))
buttonB=Button(root,text="Button B", command=lambda: use_requests())
buttonC=Button(root,text="Button C", command=lambda: endwindow())
buttonA.pack()
buttonB.pack()
buttonC.pack()
root.mainloop()
sys.exit()
