# will hold the information about the game
# such as rules about the game

class Game:
    '''
        Features:
            - return the number of mines/flags per difficulty
            - calculate game state after inputted is received
    '''
    
    def __init__(self,size):
        # body for the constructor
        pass

    # 
    def get_mines_per_size(self,size):
        '''
            returns amount of mines if a difficulty is selected
        '''
        # pre-defined options
        difficulty = {
            '8x8': 10,
            '16x16':40,
            '30x16':99
        }

        return  difficulty[size]
    

    
