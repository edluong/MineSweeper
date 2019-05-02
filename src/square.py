class Square:
    def __init__(self, row, col, mines = 0, hasFlag = False, isVisible = False ):
        self.coordinates = (row,col)
        self.mines = mines
        self.hasFlag = hasFlag
        self.isVisible = isVisible

    def place_flag(self):
        self.hasFlag = True

    def show_visible(self):
        self.isVisible = True
    
    def set_as_mine(self):
        '''
        setting the Square as a mine
        '''
        self.mines = -1
    
    def __str__(self):
        return str(self.coordinates)