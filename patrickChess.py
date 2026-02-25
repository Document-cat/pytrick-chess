import numpy as np
import re

#----Start of Bit Boards----
class bitBoard:     
    wP = np.uint64(0x00FF000000000000)
    wR = np.uint64(0x8100000000000000)
    wN = np.uint64(0x4200000000000000)
    wB = np.uint64(0x2400000000000000)
    wQ = np.uint64(0x1000000000000000)
    wK = np.uint64(0x0800000000000000)

    bP = np.uint64(0x000000000000FF00)
    bR = np.uint64(0x0000000000000081)
    bN = np.uint64(0x0000000000000042)
    bB = np.uint64(0x0000000000000024)
    bQ = np.uint64(0x0000000000000010)
    bK = np.uint64(0x0000000000000008)

    bList = [wP,wN,wB,wR,wQ,wK,bP,bN,bB,bR,bQ,bK]
    
#functions for editing Bitboards
def pieceFromBit(bitPos):
    Stb = np.uint64(0x8000000000000000)
    pieceLocation = np.right_shift(Stb, np.uint64(bitPos))

    #peiceCode generated from the order they appear in the list
    pieceCode = 0
    for var in bitBoard.bList:
        pieceCode += 1
        if np.bitwise_and(var, pieceLocation) != 0:
            return pieceCode
        else:
            continue

def moveBit(bitBoard, fromBit, toBit):
    Stb = np.uint64(0x8000000000000000)
    newBoard = np.bitwise_or(bitBoard, np.right_shift(Stb, np.uint64(toBit)))
    newBoard = np.bitwise_xor(newBoard, np.right_shift(Stb, np.uint64(fromBit)))
    return newBoard
    
def makeMove(startSq, endSq):
    pieceCode = pieceFromBit(startSq)
    match pieceCode:
        case 1:
            bitBoard.wP = moveBit(bitBoard.wP, startSq, endSq)
        case 2:
            bitBoard.wN = moveBit(bitBoard.wN, startSq, endSq)
        case 3:
            bitBoard.wB = moveBit(bitBoard.wB, startSq, endSq)
        case 4:
            bitBoard.wR = moveBit(bitBoard.wR, startSq, endSq)
        case 5:
            bitBoard.wQ = moveBit(bitBoard.wQ, startSq, endSq)
        case 6:
            bitBoard.wK = moveBit(bitBoard.wK, startSq, endSq)
        case 7:
            bitBoard.bP = moveBit(bitBoard.bP, startSq, endSq)
        case 8:
            bitBoard.bN = moveBit(bitBoard.bN, startSq, endSq)
        case 9:
            bitBoard.bB = moveBit(bitBoard.bB, startSq, endSq)
        case 10:
            bitBoard.bR = moveBit(bitBoard.bR, startSq, endSq)
        case 11:
            bitBoard.bQ = moveBit(bitBoard.bQ, startSq, endSq)
        case 12:
            bitBoard.bK = moveBit(bitBoard.bK, startSq, endSq)

#random gui utilities
def printBitBoard(bitBoard):
    bstring = (bin(bitBoard)[2:].zfill(64))
    bstring = bstring.replace("0",".")

    bList = []
    increment = 0
    while increment <= 64: 
        bList.append(bstring[increment:increment+8])
        increment += 8

    for ranks in reversed(bList):
        print(ranks)

def printBoard():
    pieceList = []

    for item in bitBoard.bList:
        pieceList.append(bin(item)[2:].zfill(64))
        
    #initialize empty board
    boardS = "................................................................"
    pieceIndex = 0
    while pieceIndex != 12:
        index = 0
        for bit in pieceList[pieceIndex]:
            if bit == "1":
                boardS = boardS[:index] + f'{pieceIndex:x}' + boardS[index+1:]
            elif boardS[index] == "." and bit == "0":
                boardS = boardS[:index] + "." + boardS[index+1:]
            index += 1
        pieceIndex += 1

    replaceTable = str.maketrans("0123456789ab", "PNBRQKpnbrqk")
    boardS = boardS.translate(replaceTable)

    output = []
    increment = 0
    while increment <= 64: 
        output.append(boardS[increment:increment+8])
        increment += 8

    for ranks in reversed(output):
        print(ranks)

def notationToChoords(notation):
    rankFrom = ord(notation[0:1])-97
    fileFrom = int(notation[1:2])-1

    rankTo = ord(notation[2:3])-97
    fileTo = int(notation[3:4])-1

    bitFrom = (8*fileFrom) + rankFrom
    bitTo = (8*fileTo) + rankTo

    if len(notation) == 5:
        return bitFrom, bitTo, notation[4:5]

    #return pieceFromBit(bitFrom), bitFrom, bitTo
    return bitFrom, bitTo
    
#----start of main----
printBoard()

x = 0
while x == 0:
    move = input("move: ")
    makeMove(*notationToChoords(move))
    printBoard()
