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
        self.row = row
        self.col = col
        self.board = [[0] * row for i in range(col)] # initialize empty board


    def print_board(self):
            '''
                method that will print out the elements inside the board
            '''
            # created a nicer print view for the user to see
            for row in range(self.row):
                for col in range(self.col):
                    # if at the end of the row
                    if col == self.col - 1:
                        # create an empty row then start on the next one
                        print(self.board[col][row],end='\n\n')
                    else:
                        # print out each row element with a tab
                        print(self.board[col][row],end='\t')
                   
                    