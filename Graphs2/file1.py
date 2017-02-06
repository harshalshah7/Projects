#author: Harshal Shah Harshal.Shah@colorado.edu
#name: file1.py
#purpose: Create a two linegraph with data from the states csv on the census.gov web site.Also use prettytables to print on the terminal.    
#date: 11/06/2016
#version: 9.1
try:
    import sys
    import os
    import matplotlib.pyplot as plt 
    import requests 
    import csv
    from prettytable import PrettyTable
except:
    print("Some modules were not correctly installed on your system")
    sys.exit()
mfg=[]
mgg=[]
m=0
list1=[]
list2=[]
list3=[]
list4=[]
list5=[]
list6=[]
xaxis1=[]
xaxis2=[]
xaxis3=[]

try:
    r=requests.get("https://www.census.gov/popest/data/counties/totals/2011/tables/CO-EST2011-01-08.csv")
except:
    print("Requested url does not exist and/or Check your Internet Connection")
    sys.exit()
abc=r.text

try:
    abc=abc.splitlines()
    n=len(abc)
    for i in abc:
        m=m+1
        if ((m > 5) and (m < (n-5))):
            
            p=i.replace(",,,,", "")
            #print(p)
            if len(p)== 5:
                f=m-1
                z=p.split(",")
                q=len(z)
                b=z[1]
                c=z[q-1]
                xaxis=z[0]
                xaxis1.append(xaxis)         
                d=b.replace("\"", "")
                e=c.replace("\"", "")
                list1.append(d)
                list3.append(e)
            else:
                f=m-1
                z=p.split(",")
                q=len(z)
                xaxis=z[0]
                xaxis2.append(xaxis)
                b=z[1]+z[2]
                c=z[q-2]+z[q-1]    
                d=b.replace("\"", "")
                e=c.replace("\"", "")
                list2.append(d)
                list3.append(e)
            list5=list1+list2
            list6=list3+list4
            xaxis3=xaxis1+xaxis2
    print(xaxis3)
    print(list5)
    print(list6)
    line1=list5
    line2=list6
    table = PrettyTable()
    table.add_column("County" , xaxis3)
    table.add_column("Observed" , list5)
    table.add_column("Estimated" , list6)
    print(table)   
    plt.xlabel("X label")
    plt.ylabel("Y Label")
    plt.title("Colorado Population Stats")
    plt.plot(line2)
    plt.plot(line1)   
    plt.legend(['Observed', 'Estimated'], loc='upper left')
    plt.xticks(range(64), xaxis3, rotation="vertical")
    plt.savefig("filename.png")
    plt.show()
except:
    print("could not parse the file")
    sys.exit()    
sys.exit()