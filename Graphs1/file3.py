##############################################################################################################
# Copyrights 2016 Harshal Shah All Rights Reserved
# The information contained herein is property of the Authors.
# The copying and distribution of the files is prohibited except by express written agreement with the Authors.
# Authors: Harshal Shah
#purpose: Create  pie chart of the cartheft.csv file
#date: 10/26/2016
###############################################################################################################
import sys
import os
import csv
import matplotlib.pyplot as plt

compname=[]
data=[]
if os.path.isfile("cartheft.csv"):
    with open('cartheft.csv') as csvfile:
        reader=csv.reader(csvfile)
        for row in reader:
            if row:
                if float(row[4]) > 2.5 :
                    data.append(row[4])
                    compname.append(row[0]+ "-" + row[1]) 
        labels=compname
        perc=data
        colors=['blue', 'red', 'purple', 'green', 'yellow', 'orange', 'pink', 'grey', 'cyan', 'crimson', 'silver']
        print("1")
        plt.title("Pie Chart")
        plt.pie(perc,colors=colors, labels=labels, autopct = '%1.1f%%', shadow=True, startangle=90)
        plt.axis('equal')
        plt.show()
else:
    print("sorry the file does not exist")
    sys.exit()            
sys.exit()    
