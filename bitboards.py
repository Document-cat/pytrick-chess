import numpy as np
import re
#----Random utils----
#sets a specific bit to 1
def bitToOne (bitString, bitPos):
	return np.bitwise_or(bitString, np.left_shift(np.uint64(1), bitPos))

#sets a specific bit to 0 if the bit was a 1
def bitToZero (bitString, bitPos):
	return np.bitwise_xor(bitString, np.left_shift(np.uint64(1), bitPos))

#prints bitboard
def printBitBoard(bitString):
	string = np.binary_repr(bitString, width=64)
	string = string.replace("0",".")
	increment = 0
	while increment != 64:
		print(string[increment:increment+8])
		increment += 8

#prints full board, takes in tuple of bitboards
def printBoard(bitboards):
	def readList(wP, wN, wB, wR, wQ, wK, bP, bN, bB, bR, bQ, bK):
		x = int(wP,16) + int(wN,16) + int(wB,16) + int(wR,16) + int(wQ,16) + int(wK,16) + int(bP,16) + int(bN,16) + int(bB,16) + int(bR,16) + int(bQ,16) + int(bK,16)
		match x:
			case 0: return "."
			case 1:	return "P"
			case 2:	return "N"
			case 3:	return "B"
			case 4:	return "R"
			case 5:	return "Q"
			case 6:	return "K"
			case 7:	return "p"
			case 8: return "n"
			case 9:	return "b"
			case 10:return "r"
			case 11:return "q"
			case 12:return "k"
	(wP, wN, wB, wR, wQ, wK, bP, bN, bB, bR, bQ, bK) = bitboards
	wP = list(np.binary_repr(wP, width=64))
	wN = list(np.binary_repr(wN, width=64).replace("1","2"))
	wB = list(np.binary_repr(wB, width=64).replace("1","3"))
	wR = list(np.binary_repr(wR, width=64).replace("1","4"))
	wQ = list(np.binary_repr(wQ, width=64).replace("1","5"))
	wK = list(np.binary_repr(wK, width=64).replace("1","6"))
	bP = list(np.binary_repr(bP, width=64).replace("1","7"))
	bN = list(np.binary_repr(bN, width=64).replace("1","8"))
	bB = list(np.binary_repr(bB, width=64).replace("1","9"))
	bR = list(np.binary_repr(bR, width=64).replace("1","A"))
	bQ = list(np.binary_repr(bQ, width=64).replace("1","B"))
	bK = list(np.binary_repr(bK, width=64).replace("1","C"))
	
	string = list(map(readList, wP, wN, wB, wR, wQ, wK, bP, bN, bB, bR, bQ, bK))
	increment = 0
	while increment != 64:
		print(*string[increment:increment+8])
		increment += 8

#Converts FEN String into bitboards
def makeBitBoards(fenString):
	posFen = fenString.split(" ", 1)[0].replace("/", "")
	
	posFen = posFen.replace("8", "00000000")
	posFen = posFen.replace("7", "0000000")
	posFen = posFen.replace("6", "000000")
	posFen = posFen.replace("5", "00000")
	posFen = posFen.replace("4", "0000")
	posFen = posFen.replace("3", "000")
	posFen = posFen.replace("2", "00")
	posFen = posFen.replace("1", "0")
	
	wP = np.uint64(int(posFen.translate(str.maketrans("pnbrqkPNBRQK","000000100000")), 2))
	wN = np.uint64(int(posFen.translate(str.maketrans("pnbrqkPNBRQK","000000010000")), 2))
	wB = np.uint64(int(posFen.translate(str.maketrans("pnbrqkPNBRQK","000000001000")), 2))
	wR = np.uint64(int(posFen.translate(str.maketrans("pnbrqkPNBRQK","000000000100")), 2))
	wQ = np.uint64(int(posFen.translate(str.maketrans("pnbrqkPNBRQK","000000000010")), 2))
	wK = np.uint64(int(posFen.translate(str.maketrans("pnbrqkPNBRQK","000000000001")), 2))
	bP = np.uint64(int(posFen.translate(str.maketrans("pnbrqkPNBRQK","100000000000")), 2))
	bN = np.uint64(int(posFen.translate(str.maketrans("pnbrqkPNBRQK","010000000000")), 2))
	bB = np.uint64(int(posFen.translate(str.maketrans("pnbrqkPNBRQK","001000000000")), 2))
	bR = np.uint64(int(posFen.translate(str.maketrans("pnbrqkPNBRQK","000100000000")), 2))
	bQ = np.uint64(int(posFen.translate(str.maketrans("pnbrqkPNBRQK","000010000000")), 2))
	bK = np.uint64(int(posFen.translate(str.maketrans("pnbrqkPNBRQK","000001000000")), 2))
	
	return wP, wN, wB, wR, wQ, wK, bP, bN, bB, bR, bQ, bK
