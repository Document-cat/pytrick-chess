import numpy as np
import re
import bitboards as bbs
import moveGen as mvg
#-------functions-------
def notationReader(notation):
	squareFrom = notation[0:2]
	squareTo = notation[2:4]
	proCheck = notation[4]
	
	
#-------main-------
fenString = input("Input Starting FEN: ")

#selects colour
colour = input("Colour (white/black): ")
if colour == "white":
	colour = 1;
else:
	colour = 0;
	
#printboards
if fenString == "":
	bbs.printBoard(bbs.makeBitBoards("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"))
else:
	bbs.printBoard(bbs.makeBitBoards(fenString))

#move functions, counter starts from 1
counter = 1
if counter % 2 == colour:
	print(notationReader(input("your move: ")))
else:
	print("thinking")
	
	
