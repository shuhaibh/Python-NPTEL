#Program to implement the Monte Carlo Program 
import random

doors=[0]*3
goatdoor=[0]*2
swap=0 #no of swap wins
dont_swap=0 #no of dont swap wins

j=0

while(j<10):
    
    x=random.randint(0,2) #xth door will comprise of BMW
    doors[x]="BMW"
    for i in range(0,3):
        if(i==x):
            continue
        else:
            doors[i]="Goat"
            goatdoor.append(i)
    
    choice=int(input("Enter your choice(0,1,2):-"))
    if choice not in [0,1,2]:
        print("Enter a Valid Number!")
        continue
    
    door_open=random.choice(goatdoor) #opens a door which has a Goat
    
    while(door_open==choice):
        door_open=random.choice(goatdoor)
    ch=input("Do you want to swap?(y/n)")
    if(ch=='y'):
        if(doors[choice]=='Goat'):
            print("Player wins")
            swap=swap+1
        else:
            print("Player Lost!")
    else:
        if(doors[choice]=='Goat'):
            print("Player lost")
        else:
            print("Player won")
            dont_swap=dont_swap+1      
            
    j=j+1
            
print(swap)
print(dont_swap)
