#functions needed

#check horizontal
#check vertical
#check tie
#check win
#create board
#def player input
gameRunning= True
winner=None 
currentPlayer="X"
board= [ "-", "-", "-",
           "-", "-", "-",
           "-", "-", "-"]
def printboard (board):
   print (board[0] + "|" + board[1] + "|" + board[2] + "|")
   print ("_________")
   print (board[3] + "|" + board[4] + "|" + board[5] + "|")
   print("_________")
   print (board[6] + "|" + board[7] + "|" + board[8] + "|")
   print("_________")




#def input

def inp(board):
    inp=int(input("Enter a value from 1-9"))
    if (inp>=1 and inp<=9 and board[inp-1]=="-"):
        board[inp-1]=currentPlayer
    else:
        print("The value you entered is not between 1 and 9")

#check for wins
def checkhorizontal (board):
    global winner
    if (board[0]== board[1]==board[2] and board[0]!="-"):
        winner=board[0]
        return True
    elif (board[3]== board[4]==board[5] and board[3]!="-"):
        winner=board[3]
        return True
    elif (board[6]== board[7]==board[8] and board[6]!="-"):
        winner==board[6]
        return True
    return False

def checkvertical (board):
    global winner
    if (board[0]== board[3]==board[6] and board[0]!="-"):
        winner==board[0]
        return True
    elif (board[1]==board[4]==board[7] and board[1]!="-"):
        winner==board[1]
        return True
    elif (board[2]== board[5]==board[8] and board[2]!="-"):
        winner==board[2]
        return True
    return False

def checkdiagonal (board):
    global winner
    if (board[0]==board[4]==board[8] and board[0]!="-"):
        winner=board[0]
        return True
    elif (board[6]==board[4]==board[2] and board[2]!="-"):
        winner=board[6]
        return True
    return False

def checktie (board):
    global gameRunning
    global winner
    if "-" not in board:
        board(board)
        print ("It is a tie!")
        gameRunning=False

def switchPlayer():
    global currentPlayer
    if currentPlayer=="X" :
        currentPlayer="0"
    else:
        currentPlayer="X"

def checkwin():
    if (checkhorizontal(board) or checkdiagonal(board) or checkvertical(board)):
        print ("the winner is" + winner)
        return True
    return False
        
        
while gameRunning:
    printboard(board)
    inp(board)
    if checkwin():
        printboard(board)
        break
    checktie(board)
    switchPlayer()
