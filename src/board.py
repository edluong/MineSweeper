from square import *

class Board:
    '''
        Features:
        - determine the size of the board -> str
        - first location will not be a mine
        - choose mine locations
        - open up locations that do not have adjacent mines
        - show numbers next to non-mine squares of how many adjacent mines
    '''
    def __init__(self,row,col):
        self.row, self.col = row, col
        self.board = [[Square(r,c) for r in range(self.row)] for c in range(self.col)] # initialize empty board

    def get_possible_squares(self) -> list:
        flat_list = []
        for row in self.board:
            for col in row:
                flat_list.append(col)
        
        return flat_list
    
    def initial_list(self,squares,coord) -> list:
        result = squares
        for square in result:
            if square.coordinates == coord:
                result.remove(square)

        return result
        
    def update_board(self,mine_list):
        for row in self.board:
            for square in row:
                if square in mine_list:
                    square.set_as_mine()
    


    def print_board(self):
        '''
            method that will print out the coordinates inside the board
        '''
        # created a nicer print view for the user to see
        for r in range(self.row):
            for c in range(self.col):
                # if at the end of the row
                if c == self.col - 1:
                    if self.board[r][c].mines == -1:
                        print(self.board[r][c].mines,end='\n\n')
                    else:
                        # create an empty row then start on the next one
                        print(self.board[r][c].coordinates,end='\n\n')
                else:
                    # print out each row element with a tab
                    #print(self.board[r][c].coordinates,end='\t')  
                    if self.board[r][c].mines == -1:
                        print(self.board[r][c].mines,end='\t')
                    else:
                        # create an empty row then start on the next one
                        print(self.board[r][c].coordinates,end='\t')                 