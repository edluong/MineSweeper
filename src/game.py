# will hold the information about the game
# such as rules about the game

class Game:
    '''
        Features:
            - return the number of mines/flags per difficulty
            - calculate game state (did the user lose?) after inputted is received
    '''
    
    def __init__(self,row,col):
        # body for the constructor
        self.row = row
        self.col = col

    # 
    def get_mines_per_size(self):
        '''
            returns amount of mines if a difficulty is selected
        '''
        # pre-defined options
        difficulty = {
            # row sizes, will then contain respective column look up
            8: {
                # column size which then will look up how many mines
                8: 10
            },
            16:{
                16: 40
            },
            30:{
                16: 99
            }
        }

        return  difficulty[self.row][self.col]

    def generate_rand_mine_list(self, possible_squares, num_of_mines):
        '''
            @param: a list of possible squares to pick from
            and how many mines there are\n
            returns: a random list of squares that will be the mine
        '''
        pass
        