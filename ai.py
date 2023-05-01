import random

def checkCapturesAi(pawnPositions,board):
    possibleCaptures=  []
    for pawn in pawnPositions:
        if pawn[0]<6:
            if pawn[1]>1:
                if board[pawn[0]+1][pawn[1]-1] == 1 and board[pawn[0]+2][pawn[1]-2] == 0:
                    capture =str(pawn[0])+ str(pawn[1])+str(pawn[0]+2)+ str(pawn[1]-2)
                    possibleCaptures.append(capture)
            if pawn[1]<6:
                if board[pawn[0]+1][pawn[1]+1] == 1 and board[pawn[0]+2][pawn[1]+2] == 0:
                    capture =str(pawn[0])+ str(pawn[1])+str(pawn[0]+2)+ str(pawn[1]+2)
                    possibleCaptures.append(capture)
    return possibleCaptures

def checkPromotionsAi(board):
    pawnPositions = getPawnPositionsAi(board)
    for pawn in pawnPositions:
        if pawn[0]==7:
            board[pawn[0]][pawn[1]]=4
    return board

def captureAi(board,move):
    posx=int(move[1])
    posy=int(move[0])
    targetx=int(move[3])
    targety=int(move[2])
    capturex=int((posx+targetx)/2)
    caputrey=int((posy+targety)/2)
    board[caputrey][capturex]=0
    return board

def checkMovesAi(pawnPositions,board):
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

def getPawnPositionsAi(board):
    pawnPositions = []
    for i,row in enumerate(board):
        for index,column in enumerate(row):
            if column==2:
                pawnPositions.append([i,index])
    return pawnPositions



def Ai(board):
    pawnPositions = getPawnPositionsAi(board)
    possibleCaputres = checkCapturesAi(pawnPositions,board)
    if len(possibleCaputres)>0:
        moreCaptures =True
        move= random.choice(possibleCaputres)
        board = captureAi(board, move)
        board = moveAi(board, move)
        board = checkPromotionsAi(board)
        pawnPositions = getPawnPositionsAi(board)
        possibleCaputres = checkCapturesAi(pawnPositions,board)
        while len(possibleCaputres)>0 and moreCaptures ==True:
            pawnPositions = getPawnPositionsAi(board)
            possibleCaputres = checkCapturesAi(pawnPositions,board)
            newCaptures = []
            newPos = move[2:]
            for capture in possibleCaputres:
                if capture[:2]==newPos:
                    newCaptures.append(capture)
            if len(newCaptures)>0:
                move= random.choice(newCaptures)
                board = captureAi(board, move)
                board = moveAi(board, move)
                board = checkPromotionsAi(board)
            else:
                moreCaptures = False    

    else:
        print(checkMovesAi(pawnPositions, board))
        possibleMoves = checkMovesAi(pawnPositions, board)
        if len(possibleMoves) >0:
            board = moveAi(board, random.choice(possibleMoves))
            board = checkPromotionsAi(board)
    return board