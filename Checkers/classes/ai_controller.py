from random import *

class AI_controller(object):
    board =[[0 for x in range(8)]for y in range(8)]
    valid_items = []
    
    def __init__(self, b):
        self.board = b


    
#will allow the computer to make a move
    def move(self,):
        self.valid_items.clear()
        valid_item = False
        coor = ""
        valid_move = False
        #look for items on the board that could be moveable
        for x in range(0,8):
            for y in range(0,8):
                valid_item = False
                valid_item = self.can_be_moved(x,y)
                if(valid_item == True):
                    coor = str(x) + "," + str(y)
                    self.valid_items.insert(-1,coor)
        
        print (self.valid_items)
        #select a random item to move
        while(valid_move == False):
        
            coor = choice(self.valid_items)
            print (coor)
            row = int(coor[0])
            col = int(coor.split(",")[-1])
            new_row = row+1
            new_col = randint(0,1)

            #will determine if the new column will be a move to the right or left
            if(new_col == 0):
                new_col = col-1
            elif(new_col == 1):
                new_col = col+1

            if(new_col <0):
                new_col = col+1
            elif(new_col >7):
                new_col = col-1

            
            valid_move = self.check_valid(row, col, new_row, new_col)
        

        return self.board

#will check if the entered move is valid
    def check_valid(self, row, col, new_row, new_col):
        valid_move = False
        if(new_col > col or new_col < col):
            if(new_col == col+1 or new_col == col-1):
                if(new_row == row+1):
                    if(self.board[new_row][new_col] != " B "):
                        self.board[row][col] = " | "
                        self.board[new_row][new_col] = " B "
                        valid_move = True
        if(self.board[row][col] == " R "):
            valid_move = False

        return valid_move


#will check if the item selected can be moved
    def can_be_moved(self, row, col):

        valid_item = False
        
        if(self.board[row][col] == " B "):
            if(col+1 > 7):
                if(self.board[row+1][col-1] != " B "  ):
                    valid_item = True
            elif(col-1<0):
                if(self.board[row+1][col+1] != " B "  ):
                     valid_item = True
            elif(col+1 <=7 or col-1 >=0):
                if(self.board[row+1][col+1] != " B " or self.board[row+1][col-1] != " B " ):
                    valid_item = True


        return valid_item
            

    
        




    
                    
        
        
        
    
