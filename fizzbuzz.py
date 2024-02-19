#A program to play a game(multiple of 3-fizz // multiple of 5-buzz // multiple of both-fizzbuzz) 
def fizzbuzz(r):
    #Program to implment the fizz buzz problem
    for i in range(1,r+1):
        if(i%3==0 and i%5==0):
            print(str(i)+":- fizzbuzz")
        else:
            if(i%3==0):
                print(str(i)+":- fizz")
            else:
                if(i%5==0):
                    print(str(i)+":- buzz")
                else:
                    print(str(i)) 
