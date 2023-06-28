import numpy as np
#from cv2 import cv2
import os
#import pandas as pd
#import functools
#from matplotlib import pyplot as plt
f=open("data.txt",'r+',encoding="utf-8")
a=f.read().splitlines()
b=len(a)
s=(b,25)
zeropadding=np.zeros(s)
#print(b)
for i in range(b):
    c=len(a[i])
    n=0
    counter=0
    #print(a[i])
    for j in range(c):
        if a[i][j] != " ":
           counter=counter+1
           if j==c-1:
               #print(j)
               d=zeropadding[i][n]
               while counter!=0:
                  d=d+int(a[i][j-counter+1])*10**(counter-1)
                  print(d)
                  counter=counter-1
               counter=0
               zeropadding[i][n]=d
               n=n+1
           continue
        elif a[i][j] == " ":
            #print(counter)
            d=zeropadding[i][n]
            while counter!=0:
                  d=d+int(a[i][j-counter])*10**(counter-1)
                  print(d)
                  counter=counter-1
            counter=0
            zeropadding[i][n]=d
            n=n+1
#print(zeropadding)
           

ff=open("data_new.dat","w+")
for i in range(b):
    c=len(zeropadding[i])
    for j in range(c):
        if j!=c-1:
           ff.write(str(zeropadding[i][j]))
           ff.write(' ')
        if j==c-1:
           ff.write(str(zeropadding[i][j]))
           ff.write("\n")
ff.close()