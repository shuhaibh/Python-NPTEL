import turtle

turtle.bgcolor("black")
fudd=turtle.Turtle()

width=5
height=7

dot_distance=25

fudd.setpos(-250,250)

def spiral(m,n):
    k=0
    l=0
    f=0
    fudd.color("white")
    '''
    k=index of starting row
    l=index of starting column
    '''
    
    while(k<m and l<n):
        if(f==1):
            fudd.right(90)
        #printing the first row from remaining row
        for i in range(l,n):
            fudd.forward(dot_distance)
            #print(a[k][i],end=" ")
        
        k+=1
        f=1
        
        fudd.right(90)
        #printing the last column from the remaining column
        for i in range(k,m):
            fudd.forward(dot_distance)
            #print(a[i][n-1],end=" ")
            
        n-=1
        
        fudd.right(90)
        if(k<m):
            #printing the last row from the remaining rows
            for i in range(n-1,l-1,-1):
                fudd.forward(dot_distance)
                #print(a[m-1][i],end=" ")
            m-=1
            
        fudd.right(90)
        if(l<n):
            #printing the first column from the remaining column 
            for i in range(m-1,k-1,-1):
                fudd.forward(dot_distance)
                #print(a[i][l],end=" ")
            l+=1
'''
a=[]
count=1
for i in range(4):
    l=[]
    for j in range(4):
        l.append(count)
        count+=1
    a.append(l)
'''
spiral(20,20)
turtle.done()
                
        
        
