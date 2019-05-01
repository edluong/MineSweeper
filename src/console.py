from .board import *
from .game import *

class Console:
    '''
        Features:
            - Let the user be able to interact with the board and game

    '''
    def __init__(self):
        self.choice = self.setup_difficulty()

        
        settings = {
            1 : (8,8), # row and column settings
            2 : (16,16),
            3 : (30,16)
        }

        # load the settings
        row = settings[self.choice][0]
        col = settings[self.choice][1]

        # initialize board and game state
        self.board = Board(row,col)
        g = Game(row,col)

        # print the initial board
        self.board.print_board()
        print(g.get_mines_per_size())


    def setup_difficulty(self):
        difficulty = """
        1. 8 x 8 ( 10 mines )
        2. 16 x 16 ( 40 mines )
        3. 30 x 16 ( 99 mines )
        """
        print(difficulty)
        return int(input('Select Difficulty (1 to 3): '))
    
    def set_initial_pick(self):
        inp = input('Square (fmt: xcoor ycoor): ')
        coord = inp.split(' ')
        row = int(coord[0])
        col = int(coord[1])
        self.initial_pick = (row,col)   # -> tuple
    
    def get_initial_pick(self):
        return self.initial_pick
    
    # test function
    def new_board(self):
        print(self.board.get_possible_locations(self.get_initial_pick()))