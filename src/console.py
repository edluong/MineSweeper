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
        self.game = Game(row,col)
        self.mine_size = self.game.get_mines_per_size()

        # print the initial board
        self.board.print_board()
        print(self.mine_size)


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
        print('list of possible choices:')
        initial_list = self.board.initial_list(self.board.get_possible_squares(),self.get_initial_pick())
        print('to see list of square objects')
        print(initial_list)
        print('list of possible Squares')
        for square in initial_list:
            print(square.coordinates)

        print('list of mines chosen:')
        mine_list = self.game.generate_rand_mine_list(initial_list,self.mine_size)
        print('Square print out')
        print(mine_list)
        print('Square coordinates of mines')
        for square in mine_list:
            print(square.coordinates)
        