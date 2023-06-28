import numpy as np
import os
import xlsxwriter



f = open('data_new.dat')
content=np.loadtxt('data_new.dat', delimiter=' ')

f.closed
row=len(content)
print(row)
c=np.zeros((row,25))
s=np.zeros(row)
for j in range(0,row-1):
    s[j]=content[j,0]

s=sorted(s)
for j in range(0,row-1):
      c[j][0]=s[j]

for j in range(0,row-1):
      for k in range(0,row-1):
          if c[j][0]==content[k,0]:
             number=0
             while number < 24:
                 c[j][number]=content[k,number]
                 number=number+1
          elif c[j][0]!=content[k,0]:
             continue
          
content=c

with open("arrangement.txt",'r+') as f:
    f.truncate(0)
f.close()
                 
[r,c]=np.shape(content)
out=np.zeros((r,2))
for x in range(0,r):
    num=1
    out[x,0]=content[x][0]
    while num < c:
        num=num+1
        out[x,1]=out[x,1]+content[x][num-1]

#print(r)
#print(c)
#print(out)
respond=input("0 or 1 ?")
respond=int(respond)

if respond == int(1):
   date_1=input("date1 :")
   date_2=input("date2 :")
   date_1=int(date_1)
   date_2=int(date_2)
   counter=np.zeros((1,2))

   for x in range(0,r):
       if out[x,0]==date_1:
           counter[0,0]=x
       if out[x,0]==date_2:
           counter[0,1]=x


   print(counter)

   i=int(counter[0,0])
   j=int(counter[0,1])
   print(i)
   print(j)
   sum=0
   x_range=np.zeros((j-i+1))
   y_range=np.zeros((j-i+1))
   for x in range(i,j+1):
       sum=sum+out[x,1]
       y_range[x-i]=out[x,1]
       x_range[x-i]=out[x,0]

   print(x_range[0])
   print(x_range[j-i])
   print('summary=')
   print(sum)
   workbook = xlsxwriter.Workbook('account.xlsx')
   worksheet = workbook.add_worksheet('sheet')

   length=len(x_range)
   length=int(length)
   print('excel_length :')
   print(length)

   for j in range(0,length):
       worksheet.write('A' + str(j+1), int(x_range[j]))
       worksheet.write('B' + str(j+1), int(y_range[j]))
   workbook.close()
   
elif respond == int(0):
   print('wish you have a nice day')
