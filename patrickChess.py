import numpy as np

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
    bK = np.uint64(0x1000000000000000)

def moveBit(bitBoard, fromBit, toBit):
    LSB = np.uint64(0x0000000000000001)
    newBoard = np.bitwise_or(bitBoard, np.left_shift(LSB, toBit))
    newBoard = np.bitwise_xor(newBoard, np.left_shift(LSB, fromBit))

def makeMove(piece, startSq, endSq):
    match piece:
        case "wP":
            bitBoard.wP = moveBit(bitBoard.wP, startSq, endSq)
        case "wR":
            bitBoard.wR = moveBit(bitBoard.wR, startSq, endSq)

def printBitBoard(bitBoard):
    bstring = (bin(bitBoard)[2:].zfill(64))
    bstring = bstring.replace("0",".")

    bList = []
    index = 0
    while index <= 64: 
        bList.append(bstring[index:index+8])
        index += 8

    for ranks in reversed(bList):
        print(ranks)

def notationToChoords(notation):
    rankFrom = ord(notation[0:1])-97
    fileFrom = int(notation[1:2])-1

    rankTo = ord(notation[2:3])-97
    fileTo = int(notation[3:4])-1

    bitFrom = (8*rankFrom) + fileFrom
    bitTo = (8*rankTo) + fileTo

    string = [bitFrom, bitTo]

    if len(notation) == 5:
        string.append(notation[4:5])

    return string
    
#----start of main---
makeMove()