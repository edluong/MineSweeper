# main file to interact with the whole program

#from src.console import * # add functions from console using the following format
from src.board import *
from src.game import *

#board = Board(30,16)
board = Board(8,8)
g = Game(8,8)

#board.print_board()


print(g.get_mines_per_size())





