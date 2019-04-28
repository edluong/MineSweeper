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

        row = settings[self.choice][0]
        col = settings[self.choice][1]

        # initialize board and game state
        board = Board(row,col)
        g = Game(row,col)

        board.print_board()
        print(g.get_mines_per_size())


    def setup_difficulty(self):
        print('1. 8 x 8 ( 10 mines )')
        print('2. 16 x 16 ( 40 mines )')
        print('3. 30 x 16 ( 99 mines )')
        return int(input('Select Difficulty (1 to 3): '))
