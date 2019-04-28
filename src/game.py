# will hold the information about the game
# such as rules about the game

class Game:
    '''
        Features:
            - return the number of mines/flags per difficulty
            - calculate game state after inputted is received
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
                8: 10
            },
            16:{
                16:40
            },
            30:{
                16:99
            }
        }

        return  difficulty[self.row][self.col]
