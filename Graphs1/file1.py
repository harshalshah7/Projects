###############################################################################################################
# Copyrights 2016 Harshal Shah All Rights Reserved
# The information contained herein is property of the Authors.
# The copying and distribution of the files is prohibited except by express written agreement with the Authors.
# Authors: Harshal Shah
#purpose: Create a line with random data  
###############################################################################################################
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
