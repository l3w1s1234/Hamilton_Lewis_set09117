from classes.controller import Controller
from classes.stack import stack
from classes.ai_controller import AI_controller
from random import *
import copy


def populate_board(board):
    
        #populates the board
    print("    0  1  2  3  4  5  6  7")
    for x in range(0, width):
        print("")
        print(x,end="  ")
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

    return board

#declared variables for the board
width =8
height = 8

board = [[0 for x in range(width)] for y in range(height)]

player_cont = Controller(board)
ai_cont = AI_controller(board)

board = populate_board(board)

undo = stack()
redo = stack()


#Start the game loop
cont = True
coor = ""
player_won = False
ai_won = False
error = False

#game loop
while(cont == True):
    if(ai_won == False):
        print("\nWhat would you like to do?\nMove or undo or end")

        #will check the entered operation
        error = True
        while(error == True):            
            coor = input()
            if(coor == "undo" and undo.isEmpty() == False):
                error = False
            elif(coor == "move"):
                error = False
            elif(coor == "end"):
                error = False
                cont = False
            else:
                
                print("Invalid input, Please enter either move or undo.")
                error = True

       
            
          
                

        #do undo if it can
        if(coor == "undo"):
            while(coor == "undo" or coor == "redo"):
                if(coor == "undo" and undo.isEmpty() == False):
                    
                    redo.push(copy.deepcopy(board))
                    board = copy.deepcopy(undo.pop())                  
                

                    

                     #display board
                    print("    0  1  2  3  4  5  6  7")
                    for x in range(0, width):
                        print("")
                        print(x,end="  ")
                        for y in range(0, height):
                            print(board[x][y], end="")
                            
                elif(coor == "redo" and redo.isEmpty() == False):
                    
                    undo.push(copy.deepcopy(board))
                    board = copy.deepcopy(redo.pop()) 



                     #display board
                    print("    0  1  2  3  4  5  6  7")
                    for x in range(0, width):
                        print("")
                        print(x,end="  ")
                        for y in range(0, height):
                            print(board[x][y], end="")
                
                print("What would you like to do?\nMove undo or redo or end")
                #will check the entered operation
                error = True
                while(error == True):
                        coor = input()
                        if(coor == "undo" and undo.isEmpty() == False):
                            error = False
                        elif(coor == "redo" and redo.isEmpty() == False):
                            error = False
                        elif(coor == "move"):
                            error = False
                        elif(coor == "end"):
                            error = False
                            cont = False
                        else:
                            print("Invalid input, Please enter either move, undo or redo.")
                            error = True

                    
                        
                       
                
                
       #do everything else if the game hasnt enced         
        if(cont == True):
            print("Enter the row and column of the checker you want to move.\n e.g. (0,0) would be the top left of the board and (7,7) would be bottom right.")
            error = True
            undo.push(copy.deepcopy(board))
            while(redo.isEmpty() == False):
                redo.pop()

        
            while(error == True):
                try:
                    coor = input()
                    board = player_cont.move(coor,board)
                    #break the loop if there was no error in the move
                    error = False
                    
                except:
                    print("Invalid input, Please re-enter the checker you want to move.")
                    error = True


        

            print("    0  1  2  3  4  5  6  7")
            #display board
            for x in range(0, width):
                print("")
                print(x,end="  ")
                for y in range(0, height):
                    print(board[x][y], end="")

            player_won = player_cont.has_won()



            #do ai's move
            if(player_won == False):
                print("\nComputers turn.")
                board = ai_cont.move(board)

                print("    0  1  2  3  4  5  6  7")
             #display board
                for x in range(0, width):
                    print("")
                    print(x,end="  ")
                    for y in range(0, height):
                        print(board[x][y], end="")

                ai_won = ai_cont.has_won()


            if(player_won == True):
                error = True
                while(error == True):
                    coor = input("Player Has won would you like to play again. Y/N?")
                    if(coor == "N" or coor == "n"):
                        cont = False
                        error = False
                    if(coor == "Y" or coor == "y"):
                        error =False
                        cont = True
                        #rePopulate board
                        board = populate_board(board)
                    if(error == True):print("Invalid input, please enter Y or N")
            if(ai_won == True):
                error = True
                while(error == True):
                    coor = input("Player Has won would you like to play again. Y/N?")
                    if(coor == "N" or coor == "n"):
                        cont = False
                        error = False
                    if(coor == "Y" or coor == "y"):
                        error =False
                        cont = True
                        #rePopulate board
                        board = populate_board(board)
                    if(error == True):print("Invalid input, please enter Y or N")

    

    


        





        

    

    



