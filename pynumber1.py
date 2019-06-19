

import numpy as np

r=int(input("Enter number of rows: "))  #take row number as input 
c=int(input("Enter number of columns: "))   # take column number as input
num=r*c

#generate a 2d array of size rxc with random numbers
a2=np.random.randint(low=1,high=100,size=num,dtype="int").reshape(r,c)


#store this 2d array in a file

f1=open("file1.txt","w+")
for i in a2:
  f1.write(str(i)+" ")
f1.close()

