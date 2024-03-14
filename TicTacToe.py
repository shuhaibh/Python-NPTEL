import numpy
board=numpy.array([['-','-','-'],['-','-','-'],['-','-','-']])
p1s='X'
p2s='O'

def check_rows(symbol):
    for r in range(3):
        count=0
        for c in range(3):
            if board[r][c]==symbol:
                count+=1
        if count==3:
            print(symbol,'won')
            return True
    return False
        
def check_columns(symbol):
    for c in range(3):
        count=0
        for r in range(3):
            if board[r][c]==symbol:
                count+=1
        if count==3:
            print("---",symbol,'won')
            return True
    return False

def check_diagonals(symbol):
    if board[0][0] == board[1][1] == board[2][2] == symbol or \
       board[0][2] == board[1][1] == board[2][0] == symbol:
        print("---",symbol, 'won')
        return True
    return False

def won(symbol):
    return check_rows(symbol) or check_columns(symbol) or check_diagonals(symbol)
 
def place(symbol):
    print()
    print(numpy.matrix(board))
    print()
    while(1):
        row=int(input("Enter row-1 or 2 or 3:"))
        column=int(input("Enter column-1 or 2 or 3:"))
        if row>0 and row<4 and column>0 and column<4 and board[row-1][column-1]=='-':
            break
        else:
            print('Invalid input.Please enter again!')
    board[row-1][column-1]=symbol
    
def play():
    for turn in range(9):
        if turn%2==0:
            print ('-----X Turn')
            place(p1s)
            if won(p1s):
                break
        else:
            print('-----O Turn')
            place(p2s)
            if won(p2s):
                break
    else:
        print('Draw')
play() 
