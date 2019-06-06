arr=input("enter numbers in ascending order").split()
def search(arr,num):
    first=0
    last=len(arr)-1
    found=-1
    while(first<=last and found==-1):
        mid=(first+last)//2
        if(int(arr[mid])==num):
            found=mid
        else:
            if(num<int(arr[mid])):
               last=mid-1
            else:
                first=mid+1
    return found
num=int(input("enter number to be searched for"))
found=search(arr,num)
if(found>=0):
    print("num found at index",found)
else:
    print("number not found")
