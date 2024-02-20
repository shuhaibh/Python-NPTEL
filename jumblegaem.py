#Program to Implement a jumble word game
import random
def choose():
     c=['ambulance','shopping','restaurant','hotel','computer','player','house','shirt','apple', 'banana', 'carrot', 'elephant', 'fireplace', 'guitar', 'happiness', 'island', 'jazz', 'kangaroo','lighthouse', 'moonlight', 'notebook', 'ocean', 'penguin','rainbow', 'sunset', 'telescope', 'umbrella', 'victory', 'whisper', 'xylophone', 'yoga']
     picked_word=random.choice(c)
     return picked_word
def jumble(word):
     jumble="".join(random.sample(word,len(word)))
     return jumble
def thank(p1n,p2n,p1,p2):
    print('')
    print(p1n,"Your score is :-",p1)
    print(p2n,"Your score is :-",p2)
    if(p1>p2):
        print("Congrats",p1n,"You have won")
    else:
        print("Congrats",p2n,"You have won")
    print("Thanks for playing")
    print("Have a nice day!")
def play():
    p1name=input("Player 1,Enter Your Name:-")
    p2name=input("Player 2,Enter Your Name:-")
    pp1=0
    pp2=0
    turn=0
    while(1):
        #Computers Task
        picked_word=choose()
        qn=jumble(picked_word)
        print("The word is :- ",qn)
        if turn%2==0:
            print('---',p1name,'Your turn:')
            ans=input('What is on your mind:-')
            if ans==picked_word:
                print("YAY! you guessed correct")
                pp1=pp1+1
                print("Your score is:-",pp1)
            else:
                print("Sorry wrong answer ,I thought",picked_word)
            c=int(input("Press 1 to continue or 0 to Quit:-"))
            if c==0:
                thank(p1name,p2name,pp1,pp2)
                break
            if(c!=1 and c!=0):
                print("Invalid Input!Enter again")                
        else:
            print('---',p2name,'Your turn ')
            ans=input('What is on your mind:-')
            if ans==picked_word:
                print("YAY! you guessed correct")
                pp2=pp2+1
                print("Your score is:-",pp2)
            else:
                print("Sorry wrong answer ,I thought ",picked_word)
            c=int(input("Press 1 to continue or 0 to Quit:-"))
            if c==0:
                thank(p1name,p2name,pp1,pp2)
                break
            if(c!=1 and c!=0):
                print("Invalid Input!Enter again")                
        turn=turn+1
play()
