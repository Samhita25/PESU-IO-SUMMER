number=input("enter numbers in ascending order seperated by a space").split()
flag=0
i=0
while (flag!=1):
    print(number[i],end=',')
    #print (flag)
    i=i+1
    if(int(number[i])>237):
        flag=1
        break
