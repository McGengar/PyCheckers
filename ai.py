import random

def checkCaptures(board):
    pass

def checkMoves(pawnPositions,board):
    possibleMoves = []
    for pawn in pawnPositions:
        posx=pawn[1]
        posy=pawn[0]
        if posy<7:
            if posx>0 and board[posy+1][posx-1]==0:
                targetx=posx-1
                targety=posy+1
                possibleMoves.append(str(posy)+str(posx)+str(targety)+str(targetx))
            if posx<7 and board[posy+1][posx+1]==0:
                targetx=posx+1
                targety=posy+1
                possibleMoves.append(str(posy)+str(posx)+str(targety)+str(targetx))
    return possibleMoves

def moveAi(board, move):
    posx=int(move[1])
    posy=int(move[0])
    targetx=int(move[3])
    targety=int(move[2])
    pawn = board[posy][posx]
    board[posy][posx]=0
    board[targety][targetx]=pawn
    return board

def getPawnPositions(board):
    pawnPositions = []
    for i,row in enumerate(board):
        for index,column in enumerate(row):
            if column==2:
                pawnPositions.append([i,index])
    return pawnPositions

def aiMove(board):
    pawnPositions = getPawnPositions(board)
    #checkCaptures(board)
    print(checkMoves(pawnPositions, board))
    possibleMoves = checkMoves(pawnPositions, board)
    board = moveAi(board, random.choice(possibleMoves))
    return board