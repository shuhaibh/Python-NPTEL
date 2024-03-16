# A Program to implement the dobble game 
import string
import random
op=1
while(op==1):
    symbols=[]
    symbols=list(string.ascii_letters)
    card1=[0]*5
    card2=[0]*5
    pos1=random.randint(0,4)
    pos2=random.randint(0,4)
    #pos1 and pos2 are the same symbol position
    samesymbol=random.choice(symbols)
    symbols.remove(samesymbol)
    if(pos1==pos2):
        card1[pos1]=samesymbol
        card2[pos2]=samesymbol
    else:
        card1[pos1]=samesymbol
        card2[pos2]=samesymbol
        card1[pos2]=random.choice(symbols)
        symbols.remove(card1[pos2])
        card2[pos1]=random.choice(symbols)
        symbols.remove(card2[pos1])
    i=0
    while(i<5):
        if(i!=pos1 and i!=pos2):
            alpha1=random.choice(symbols)
            symbols.remove(alpha1)
            alpha2=random.choice(symbols)
            symbols.remove(alpha2)
            card1[i]=alpha1
            card2[i]=alpha2
        i=i+1
    print(card1)
    print()
    print(card2)
    ch=input("Spot the similar symbol:-")
    if(ch==samesymbol):
        print("Right")
    else:
        print("wrong")
    op=input("Do you wish to continue(1/0):-")
    if(op!=1):
        print("Thanks for playing")
