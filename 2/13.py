'''Please  write  a  program  to  randomly  generate  a  list  with  5  numbers,  
which  are divisible by 5 and 7 , between 1 and 1000 inclusive
'''

ls=[]
for i in range(1,1000):
    if ((i%5==0)and(i%7==0)):
        ls.append(i)

print(ls)