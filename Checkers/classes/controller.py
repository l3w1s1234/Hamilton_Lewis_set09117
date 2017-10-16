class Controller(object):
    board =[[0 for x in range(8)]for y in range(8)]

    def __init__(self, b):
        self.board = b


    
#will take a players inputs and make sure that they are valid
    def move(self, coor):
        row = int(coor[0])
        col = int(coor.split(",")[-1])
        can_move = False
        valid_item = self.can_be_moved(row, col)

    
        while(valid_item == False):
            print("No item that can be moved, Please re enter")
            coor = input()
            row = int(coor[0])
            col = int(coor.split(",")[-1])
            valid_item = self.can_be_moved(row, col)
        
        
        if(valid_item == True):
            print("Has an item where would you like to move to?")
            coor = input()
            new_row = int(coor[0])
            new_col = int(coor.split(",")[-1])

        
        can_move = self.check_valid(row, col, new_row, new_col)
        
        while(can_move == False):
            print("Invalid Move, try a new one.")
            coor = input()
            new_row = int(coor[0])
            new_col = int(coor.split(",")[-1])
            can_move = self.check_valid(row, col, new_row, new_col)

        return self.board

#will check if the entered move is valid
    def check_valid(self, row, col, new_row, new_col):
        valid_move = False
        if(new_col > col or new_col < col):
            if(new_col == col+1 or new_col == col-1):
                if(new_row == row-1):
                    if(self.board[new_row][new_col] != " R "):
                        self.board[row][col] = " | "
                        self.board[new_row][new_col] = " R "
                        valid_move = True
        if(self.board[new_row][new_col] == " B "):
            valid_move = False

        return valid_move


#will check if the item selected can be moved
    def can_be_moved(self, row, col):

        valid_item = False

        if(self.board[row][col] == " R "):
            if(col+1 > 7):
                if(self.board[row-1][col-1] != " R "  ):
                    valid_item = True
            elif(col-1<0):
                if(self.board[row-1][col+1] != " R "  ):
                    valid_item = True
            elif(col+1 <=7 or col-1 >=0):
                if(self.board[row-1][col+1] != " R " or self.board[row-1][col-1] != " R " ):
                    valid_item = True
        

        return valid_item
            

    
        




    
                    
        
        
        
    
