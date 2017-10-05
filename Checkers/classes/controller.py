class Controller:
    board=[[0 for x in range(10)]for y in range(10)]

    def __init__(self, b):
        self.board = b

#will handle movements
    def move(self, coor):
        x = int(coor[0])
        y = int(coor.split(",")[-1])

        if(board[x][y] == " R "):
            print("Has an item where would you like to move to?")
            coor = input()
            new_x = int(coor[0])
            new_y = int(coor.split(",")[-1])

            if(new_x > x or new_x < x):
                if(new_x == x+1 or new_x == x-1):
                    if(y == y+1):
                        board[x][y] = " | "
                        board[new_x][new_y] = " R "
        elif(board[x][y] == " | " or board[x][y] == " B "):
            print("Invalid move try again.")
                    
        
        
        
    
