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
        is_a_king = False

        if(self.board[row][col] == " K "):is_a_king = True

        
        
        if(self.board[new_row][new_col] == " B "):
            if(new_col <7 and new_col >0):
                valid_move = self.jump_counter(row, col, new_row, new_col)
                if(valid_move == True):
                    print("Player jumped counter at space ", new_row, ",", new_col)
        elif(new_col > col or new_col < col and valid_move != True and is_a_king == False):
            if(new_col == col+1 or new_col == col-1):
                if(new_row == row-1):
                    if(self.board[new_row][new_col] == " | " and new_row != 0):
                        #changes items on the board
                        self.board[row][col] = " | "
                        self.board[new_row][new_col] = " R "
                        valid_move = True
                    elif(self.board[new_row][new_col] == " | "  and new_row == 0):
                        #changes items on the board and kings the counter
                        self.board[row][col] = " | "
                        self.board[new_row][new_col] = " K "
                        valid_move = True
        elif(new_col > col or new_col < col and valid_move != True and is_a_king == True):
            if(new_col == col+1 or new_col == col-1):
                if(new_row > row or new_row<row):
                    if(self.board[new_row][new_col] == " | "):
                        #changes items on the board and kings the counter
                        self.board[row][col] = " | "
                        self.board[new_row][new_col] = " K "
                        valid_move = True
                        
                    
                
            
                
            
        

        return valid_move


#will check if the item selected can be moved
    def can_be_moved(self, row, col):

        valid_item = False

        if(self.board[row][col] == " R "):
            if(col+1 > 7):
                if(self.board[row-1][col-1] != " | " ):
                    valid_item = True
                elif(self.board[row-1][col-1] == " B " and self.board[row-2][col-2] == " | "):
                    valid_item = True
            elif(col-1<0):
                if(self.board[row-1][col+1] == " | "):
                    valid_item = True
                elif(self.board[row-1][col+1] == " B " and self.board[row-2][col+2] == " | "):
                    valid_item = True
            elif(col+1 <=7 or col-1 >=0):
                if(self.board[row-1][col+1] == " | " or self.board[row-1][col-1] == " | " ):
                    valid_item = True

                elif(self.board[row-1][col+1] == " B " and self.board[row-2][col+2] == " | "):
                    valid_item = True
                elif(self.board[row-1][col-1] == " B " and self.board[row-2][col-2] == " | "):
                    valid_item = True
                            
        if(self.board[row][col] == " K "):
            if(col+1 > 7):
                if(self.board[row-1][col-1] != " | " ):
                    valid_item = True
                elif(self.board[row-1][col-1] == " B " and self.board[row-2][col-2] == " | "):
                    valid_item = True
            elif(col-1<0):
                if(self.board[row-1][col+1] == " | "):
                    valid_item = True
                elif(self.board[row-1][col+1] == " B " and self.board[row-2][col+2] == " | "):
                    valid_item = True
            elif(col+1 <=7 or col-1 >=0):
                if(self.board[row-1][col+1] == " | " or self.board[row-1][col-1] == " | " ):
                    valid_item = True

                elif(self.board[row-1][col+1] == " B " and self.board[row-2][col+2] == " | "):
                    valid_item = True
                elif(self.board[row-1][col-1] == " B " and self.board[row-2][col-2] == " | "):
                    valid_item = True
            
        

        return valid_item

#will check if the counter can be jumped and will change the board accordingly, and return if it can or not
    def jump_counter(self, row, col, new_row, new_col):

        can_jump = False
        valid_move = False

        #check if the counter can be jumped
        
        if(new_col + 1 <=7 or new_col-1>=0):
            if(new_row - 1 >=0 or new_row + 1 <=7):

                if(new_col > col):   
                    if(self.board[new_row-1][new_col+1] == " | " ):
                        can_jump = True
                        valid_move = True
                if(new_col < col):
                    if(self.board[new_row-1][new_col-1] == " | ") :
                        can_jump = True
                        valid_move = True

        #do a loop that willl jump the counter as many times as it can
        while(can_jump == True):

            if(new_col > col):
            
                #change the board accordingly
                if(new_row-1 != 0):
                    self.board[row][col] = " | "
                    self.board[new_row][new_col] = " | "
                    self.board[new_row-1][new_col+1] = " R "
                elif(new_row-1 == 0):
                    self.board[row][col] = " | "
                    self.board[new_row][new_col] = " | "
                    self.board[new_row-1][new_col+1] = " K "
                    

                #will change the variables so it can check if another counter can be jumped
                row = new_row-1
                col = new_col+1

            elif(new_col < col):
                #change the board accordingly
                if(new_row-1 != 0):
                    self.board[row][col] = " | "
                    self.board[new_row][new_col] = " | "
                    self.board[new_row-1][new_col-1] = " R "
                elif(new_row-1 == 0):
                    self.board[row][col] = " | "
                    self.board[new_row][new_col] = " | "
                    self.board[new_row-1][new_col-1] = " K "

                #will change the variables so it can check if another counter can be jumped
                row = new_row-1
                col = new_col-1
                
            #check if the another jump can made
            if(row-1 >= 0 or row+1 <=7):
                if(col + 1 < 7): 
                    if(self.board[row-1][col+1] == " B "):
                        new_row = row-1
                        new_col = col+1
                elif(col-1>0):
                    if(self.board[row-1][col-1] == " B "):
                        new_row = row - 1
                        new_col = col - 1
                
            if(new_col>col):
                if(new_col+1 > 7):
                    can_jump = False
                elif(self.board[new_row][new_col] == " B " ):
                    if(new_row - 1 <0 or new_row+1 >7):
                        can_jump = False
                    elif(self.board[new_row-1][new_col+1] != " | " ):
                        can_jump = False
            elif(new_col<col):
                if(new_col-1 < 0):
                    can_jump = False
                if(self.board[new_row][new_col] == " B " ):
                    if(new_row - 1 <0 or new_row+1 >7):
                        can_jump = False
                    elif(self.board[new_row-1][new_col-1] != " | "):
                        can_jump = False




            if(self.board[new_row][new_col] != " B "):
                    can_jump  = False

                    
        

        return valid_move

                
            

        

        
            

    
        




    
                    
        
        
        
    
