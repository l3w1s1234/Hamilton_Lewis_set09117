from classes.controller import Controller

width =10
height = 10

board = [[0 for x in range(width)] for y in range(height)]

#populates the board
for x in range(0, width):
    print("")
    #will check if the space is meant to have a  checker on it
    for y in range(0, height):
        #if row is the top 3 on the board
        if(x < 4 and (x % 2) != 0):
            if(y % 2 == 0):
                board[x][y] = " B "
                print(board[x][y], end="")
            elif(y % 2 != 0):
                board[x][y] = " | "
                print(board[x][y], end="")
        elif(x < 4 and (x % 2) == 0):
            if(y % 2 == 0):
                board[x][y] = " | "
                print(board[x][y], end="")
            elif(y % 2 != 0):
                board[x][y] = " B "
                print(board[x][y], end="")
        #if the middle 2 rows
        elif(x >= 4 and x <6):
            board[x][y] = " | "
            print(board[x][y], end="")
        #if row is the bottom 3 on the board
        elif(x >= 6 and (x % 2) != 0):
            if(y % 2 == 0):
                board[x][y] = " R "
                print(board[x][y], end="")
            elif(y % 2 != 0):
                board[x][y] = " | "
                print(board[x][y], end="")
        elif(x >= 6 and (x % 2) == 0):
            if(y % 2 == 0):
                board[x][y] = " | "
                print(board[x][y], end="")
            elif(y % 2 != 0):
                board[x][y] = " R "
                print(board[x][y], end="")


#Start the game loop
cont = True


        





        

    

    



