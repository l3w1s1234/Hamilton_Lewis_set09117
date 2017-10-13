from classes.controller import Controller
from classes.stack import stack



width =8
height = 8

board = [[0 for x in range(width)] for y in range(height)]

player_cont = Controller(board)

#populates the board
for x in range(0, width):
    print("")
    #check valid spaces for checkers
    for y in range(0, height):
        #if row is the top 3 on the board
        if(x < 3 and (x % 2) != 0):
            if(y % 2 == 0):
                board[x][y] = " B "
                print(board[x][y], end="")
            elif(y % 2 != 0):
                board[x][y] = " | "
                print(board[x][y], end="")
        elif(x < 3 and (x % 2) == 0):
            if(y % 2 == 0):
                board[x][y] = " | "
                print(board[x][y], end="")
            elif(y % 2 != 0):
                board[x][y] = " B "
                print(board[x][y], end="")
        #if the middle 2 rows
        elif(x >= 2 and x <5):
            board[x][y] = " | "
            print(board[x][y], end="")
        #if row is the bottom 3 on the board
        elif(x >= 5 and (x % 2) != 0):
            if(y % 2 == 0):
                board[x][y] = " R "
                print(board[x][y], end="")
            elif(y % 2 != 0):
                board[x][y] = " | "
                print(board[x][y], end="")
        elif(x >= 5 and (x % 2) == 0):
            if(y % 2 == 0):
                board[x][y] = " | "
                print(board[x][y], end="")
            elif(y % 2 != 0):
                board[x][y] = " R "
                print(board[x][y], end="")


#Start the game loop
cont = True
coor = ""



while(cont == True):
    print("\nEnter the row and column of the checker you want to move.\n e.g. (0,0) would be the top left of the board and (7,7) would be bottom right.")
    coor = input()

    board = player_cont.move(coor)

    #display board
    for x in range(0, width):
        print("")
        for y in range(0, height):
            print(board[x][y], end="")


        





        

    

    



