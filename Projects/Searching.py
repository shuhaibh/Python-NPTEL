def Linear_Search(n,x):
    element=[]
    for i in range(1,n):
        element.append(i)
    
    count=0
    flag=0
    for i in element:
        count+=1
        if(i==x):
            print("The number is found at position:-"+str(i))
            flag=1
            break
        
    if (flag==0):
        print("The number is not found!")
        
    print("Number of iterations:" +str(count))
Linear_Search(50,14)

    
def Binary_Search(a,x):
    front=0
    end=len(a)-1
    flag=0
    count=0
    
    while(front<=end and flag==0):
        count+=1
        mid=(front+end)//2
        if(x==a[mid]):
            flag=1
            print("The Element is found at position" +str(mid))
            print("the number of iterations"+str(count))
            return
        else:
            if(x<a[mid]):
                end=mid-1
            else:
                front=mid+1
                
    print("the number is not present")
        
a=[]
for i in range(1,501):
    a.append(i)
Binary_Search(a,70)
