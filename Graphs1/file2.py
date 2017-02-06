##################################################################################################################
# Copyrights 2016 Harshal Shah All Rights Reserved
# The information contained herein is property of the Authors.
# The copying and distribution of the files is prohibited except by express written agreement with the Authors.
# Authors: Harshal Shah
# #date: 10/26/2016
#purpose:Create a bar graph of the state and their population
##################################################################################################################
import sys
import matplotlib.pyplot as plt
import numpy as np
import csv
import os
xaxis=[]
yaxis=[]
print("State population".rjust(20))
if os.path.isfile("statepop.csv"):
    
    with open('statepop.csv') as csvfile:
        reader=csv.reader(csvfile)
        for row in reader:
            if row:
                xaxis.append(row[0])
                yaxis.append(int(row[1])) 
        print(xaxis)
        print(yaxis)
        groups=len(yaxis)
        index=np.arange(groups)
        barWidth=0.5
        plt.bar(index, yaxis, barWidth, color='r')
        plt.xlabel("X label")
        plt.ylabel("Y Label")
        plt.title("Bar Chart")
        plt.xticks(index+barWidth, xaxis, rotation="vertical")
        plt.show()
else:
    print("sorry the file does not exist")
    sys.exit()            
sys.exit()    
