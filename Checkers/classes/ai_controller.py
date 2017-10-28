from random import *


class AI_controller(object):
    board =[[0 for x in range(8)]for y in range(8)]
    valid_items = []
    possible_jumps = []
    captured_counters = 0
    
    def __init__(self, b):
        self.board = b


    
#will allow the computer to make a move
    def move(self,):
        self.valid_items.clear()
        self.possible_jumps.clear()
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
        
        print(self.possible_jumps)
        #select a random item to move
        while(valid_move == False):

            #ill check if any counters can be jumped and then jump a random one
            if(len(self.possible_jumps) != 0):
                coor = choice(self.possible_jumps)
                row = int(coor[0])
                col = int(coor.split(",")[-1])
                print (coor)

                #do a jump for normal counter
                if(self.board[row][col] == " B "):
                    if(col+2<=7):    
                        if(self.board[row+1][col+1] == " R " and self.board[row+2][col+2] == " | " and valid_move == False):
                            new_row = row+1
                            new_col = col+1
                            valid_move = self.jump_counter(row,col,new_row,new_col)
                            print("Computer jumped counter at",new_row,",",new_col)

                    if(col-2>=0):
                        if(self.board[row+1][col-1] == " R " and self.board[row+2][col-2] == " | " and valid_move == False):
                            new_row = row+1
                            new_col = col-1
                            valid_move = self.jump_counter(row,col,new_row,new_col)
                            print("Computer jumped counter at",new_row,",",new_col)

               #do a jump for a kinged piece
                if(self.board[row][col] == " Q "):

                    if(row+2 <= 7):
                        if(col+2<=7):
                            if(self.board[row+1][col+1] == " R " and self.board[row+2][col+2] == " | " and valid_move == False):
                                new_row = row+1
                                new_col = col+1
                                valid_move = self.jump_counter(row,col,new_row,new_col)
                                print("Computer jumped counter at",new_row,",",new_col)
                        if(col-2>=0):
                            if(self.board[row+1][col-1] == " R " and self.board[row+2][col-2] == " | " and valid_move == False):
                                new_row = row+1
                                new_col = col-1
                                valid_move = self.jump_counter(row,col,new_row,new_col)
                                print("Computer jumped counter at",new_row,",",new_col)
                    if(row-2 >= 0):
                        if(col+2<=7):
                            
                            if(self.board[row-1][col+1] == " R " and self.board[row-2][col+2] == " | " and valid_move == False):
                                new_row = row-1
                                new_col = col+1
                                valid_move = self.jump_counter(row,col,new_row,new_col)
                                print("Computer jumped counter at",new_row,",",new_col)
                        if(col-2>=0):
                            if(self.board[row-1][col-1] == " R " and self.board[row-2][col-2] == " | " and valid_move == False):
                                new_row = row-1
                                new_col = col-1
                                valid_move = self.jump_counter(row,col,new_row,new_col)
                                print("Computer jumped counter at",new_row,",",new_col)



                        
            #will do a move that isnt a jump
            if(valid_move == False):
                
                coor = choice(self.valid_items)
                row = int(coor[0])
                col = int(coor.split(",")[-1])
                rand_comp = {1, -1}
                new_row = row+1

                
                #determine what way a kinged piece will move
                if(self.board[row][col] == " Q "):
                    if(row+1==7):
                        new_row = row-1
                    if(row==0):
                        new_row =row+1
                    if(row>0 and row<7):
                        new_row = + choice(rand_comp)
                    
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

                print("Computer moved counter at",coor," to ",new_row,",",new_col)
        

        return self.board

#will check if the entered move is valid
    def check_valid(self, row, col, new_row, new_col):
        valid_move = False
        is_a_king = False

        if(self.board[row][col] == " Q "):is_a_king = True
        
        
        if(valid_move != True and is_a_king == False):
            if(new_col == col+1 or new_col == col-1):
                if(new_row == row+1):
                    if(self.board[new_row][new_col] == " | " and new_row != 7):
                        self.board[row][col] = " | "
                        self.board[new_row][new_col] = " B "
                        valid_move = True
                    elif(self.board[new_row][new_col] == " | "  and new_row == 7):
                        #changes items on the board and kings the counter
                        self.board[row][col] = " | "
                        self.board[new_row][new_col] = " Q "
                        valid_move = True
        elif(valid_move != True and is_a_king == True):
            if(new_col == col+1 or new_col == col-1):
                if(new_row == row+1 or new_row == row-1):
                    if(self.board[new_row][new_col] == " | "):
                        #changes items on the board and kings the counter
                        self.board[row][col] = " | "
                        self.board[new_row][new_col] = " Q "
                        valid_move = True





        

        return valid_move


#will check if the item selected can be moved
    def can_be_moved(self, row, col):

        valid_item = False
        valid_move = False


        #will check if the counter can be jumped and put it into the possible jumps list
        if(self.board[row][col] == " B " ):
            if(col+1<7):
                if(self.board[row+1][col+1] == " R " or self.board[row+1][col+1] == " K "):
                    new_row = row+1
                    new_col = col+1
                    valid_move = self.check_jump(row, col, new_row, new_col)
                if(valid_move == True):
                    coor = str(row)+ "," + str(col)
                    self.possible_jumps.insert(-1,coor)
            if(col-1>0):
                if(self.board[row+1][col-1] == " R "or self.board[row+1][col-1] == " K "):
                    new_row = row+1
                    new_col = col-1
                    valid_move = self.check_jump(row, col, new_row, new_col)
                if(valid_move == True):
                    coor = str(row)+ "," + str(col)
                    self.possible_jumps.insert(-1,coor)

        #checks if kinged piece can jump counter
        if(self.board[row][col] == " Q "):
            if(col+1<7):
                if(row+1 <7):
                    if(self.board[row+1][col+1] == " R " or self.board[row+1][col+1] == " K "):
                        new_row = row+1
                        new_col = col+1
                        valid_move = self.check_jump(row, col, new_row, new_col)
                    if(valid_move == True):
                        coor = str(row)+ "," + str(col)
                        self.possible_jumps.insert(-1,coor)

                if(row-1>0):
                    if(self.board[row-1][col+1] == " R " or self.board[row-1][col+1] == " K "):
                        new_row = row+1
                        new_col = col+1
                        valid_move = self.check_jump(row, col, new_row, new_col)
                    if(valid_move == True):
                        coor = str(row)+ "," + str(col)
                        self.possible_jumps.insert(-1,coor)
                
            if(col-1>0):
                if(row+1 <7):
                    if(self.board[row+1][col-1] == " R "or self.board[row+1][col-1] == " K "):
                        new_row = row+1
                        new_col = col-1
                        valid_move = self.check_jump(row, col, new_row, new_col)
                    if(valid_move == True):
                        coor = str(row)+ "," + str(col)
                        self.possible_jumps.insert(-1,coor)
                if(row-1>0):
                    if(self.board[row-1][col-1] == " R " or self.board[row-1][col-1] == " K "):
                        new_row = row+1
                        new_col = col-1
                        valid_move = self.check_jump(row, col, new_row, new_col)
                    if(valid_move == True):
                        coor = str(row)+ "," + str(col)
                        self.possible_jumps.insert(-1,coor)
        


        #check if there is free space to move too                      
        if(self.board[row][col] == " B "):
            if(col+1 > 7):
                if(self.board[row+1][col-1] == " | " ):
                    valid_item = True
                
            if(col-1<0):
                if(self.board[row+1][col+1] == " | "):
                    valid_item = True
                
            if(col+1 <=7 and col-1 >=0):
                if(self.board[row+1][col+1] == " | " or self.board[row+1][col-1] == " | " ):
                    valid_item = True

        

        #movements for a kinged piece                    
        if(self.board[row][col] == " Q "):
            if(col+1 < 7):
                if(row+1 <7):
                    if(self.board[row+1][col+1] == " | " ):
                        valid_item = True
                if(row - 1 >0):
                    if(self.board[row-1][col+1] == " | " ):
                        valid_item = True
                
            if(col-1>0):
                if(row +1 <7):
                    if(self.board[row+1][col-1] == " | " ):
                        valid_item = True
                if(row - 1 >0):
                    if(self.board[row-1][col-1] == " | " ):
                        valid_item = True
                
            

            

        return valid_item



    #will check if the counter can be jumped and will change the board accordingly, and return if it can or not
    def jump_counter(self, row, col, new_row, new_col):

        can_jump = True
        valid_move = False

       


        #will change the board for a kinged pieces jump
        if(can_jump == True and self.board[row][col] == " Q "):
            if(new_col > col):

                self.board[row][col] = " | "
                self.board[new_row][new_col] = " | "
                if(new_row > row):
                    self.board[new_row+1][new_col+1] = " Q "
                elif(new_row < row):
                    self.board[new_row-1][new_col+1] = " Q "
                self.captured_counters += 1
                

                
                    
                    

            elif(new_col < col):
                self.board[row][col] = " | "
                self.board[new_row][new_col] = " | "
                if(new_row > row):
                    self.board[new_row+1][new_col-1] = " Q "
                elif(new_row < row):
                    self.board[new_row-1][new_col-1] = " Q "
                self.captured_counters += 1



            valid_move = True
            can_jump = False

        #do a loop that willl jump the counter as many times as it can
        while(can_jump == True):
            self.captured_counters += 1

            if(new_col > col):
            
                #change the board accordingly
                if(new_row+1 != 7):
                    self.board[row][col] = " | "
                    self.board[new_row][new_col] = " | "
                    self.board[new_row+1][new_col+1] = " B "
                elif(new_row+1 == 7):
                    self.board[row][col] = " | "
                    self.board[new_row][new_col] = " | "
                    self.board[new_row+1][new_col+1] = " Q "
                

                #will change the variables so it can check if another counter can be jumped
                row = new_row+1
                col = new_col+1

            elif(new_col < col):
                 #change the board accordingly
                if(new_row+1 != 7):
                    self.board[row][col] = " | "
                    self.board[new_row][new_col] = " | "
                    self.board[new_row+1][new_col-1] = " B "
                elif(new_row+1 == 7):
                    self.board[row][col] = " | "
                    self.board[new_row][new_col] = " | "
                    self.board[new_row+1][new_col-1] = " Q "
                
            #check if more jumps can be made
            if(col + 2 <= 7 and row+2 <=7): 
                if(self.board[row+1][col+1] == " R "and self.board[row+2][col+2] == " | "):
                    new_row = row-1
                    new_col = col+1
            if(col-1>=0 and row+2 <=7):
                if(self.board[row+1][col-1] == " R "and self.board[row+2][col-2] == " | "):
                    new_row = row - 1
                    new_col = col - 1
                
            if(new_col>col):
                if(new_col+1 > 7):
                    can_jump = False
                elif(self.board[new_row][new_col] == " R " ):
                    if(self.board[new_row+1][new_col+1] != " | " ):
                        can_jump = False
            elif(new_col<col):
                if(new_col-1 < 0):
                    can_jump = False
                if(self.board[new_row][new_col] == " R " ):
                    if(self.board[new_row+1][new_col-1] != " | "):
                        can_jump = False




            if(self.board[new_row][new_col] != " R "):
                    can_jump  = False

            valid_move = True

        return valid_move
            
    #check if the counter can be jumped
    def check_jump(self, row, col, new_row, new_col):
        can_jump = False


        if(new_col+1<=7):
            if(new_row+1 <= 7):   
                    if(self.board[new_row+1][new_col+1] == " | " ):
                        can_jump = True

            if(new_row-1 >= 0):
                if(new_col > col):   
                    if(self.board[new_row-1][new_col+1] == " | " ):
                        can_jump = True


        if(new_col-1>=0):
            if(new_row+1 <= 7):
                    if(self.board[new_row+1][new_col-1] == " | ") :
                        can_jump = True

            if(new_row-1 >= 0):   
                    if(self.board[new_row-1][new_col-1] == " | " ):
                        can_jump = True
                        

        

        return can_jump




    #will return a true false value if game has been won
    def has_won(self):
        if(self.captured_counters == 12):return True
        else: return False


    
                    
        
        
        
    
