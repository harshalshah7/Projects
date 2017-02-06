#author: Harshal Shah Harshal.Shah@colorado.edu
#name: file1.py
#purpose: Create a line with random data
#date: 10/26/2016
#version: 8.1
  
  
import sys
import random
import matplotlib.pyplot as plt
y=[]
for i in range (0, 25):
    x= random.randint(10,100) 
    y.append(x)
plt.plot(y,color='black')
plt.xlabel("Other numbers")
plt.ylabel("Random Numbers")
plt.title("My first graph")
    
print(y)
plt.show()
sys.exit()