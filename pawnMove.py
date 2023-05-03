
def move(board, pos, target):
    posx=int(ord(pos[0].lower())-97)
    posy=8-int(pos[1])
    targetx=int(ord(target[0].lower())-97)
    targety=8-int(target[1])
    pawn = board[posy][posx]
    board[posy][posx]=0
    board[targety][targetx]=pawn
    return board

def getPawnPositions(board):
    pawnPositions = []
    for i,row in enumerate(board):
        for index,column in enumerate(row):
            if column==1:
                pawnPositions.append([i,index])
    return pawnPositions

def checkPromotions(board):
    pawnPositions = getPawnPositions(board)
    for pawn in pawnPositions:
        if pawn[0]==0:
            board[pawn[0]][pawn[1]]=3
    return board

def checkCaptures(board):
    pawnPositions = getPawnPositions(board)
    possibleCaptures = set()

    for pawn in pawnPositions:
        if pawn[0]>1:
            if pawn[1]>1:
                if board[pawn[0]-1][pawn[1]-1] == 2 and board[pawn[0]-2][pawn[1]-2] == 0:
                    capture =(str(chr(pawn[1]+97))+ str(8-pawn[0]),str(chr(pawn[1]-2+97))+ str(8-pawn[0]+2))
                    possibleCaptures.add(capture)
            if pawn[1]<6:
                if board[pawn[0]-1][pawn[1]+1] == 2 and board[pawn[0]-2][pawn[1]+2] == 0:
                    capture =(str(chr(pawn[1]+97))+ str(8-pawn[0]), str(chr(pawn[1]+2+97))+ str(8-pawn[0]+2))
                    possibleCaptures.add(capture)
    
    return possibleCaptures

def capture(board,pos,target):
    posx=int(ord(pos[0].lower())-97)
    posy=8-int(pos[1])
    targetx=int(ord(target[0].lower())-97)
    targety=8-int(target[1])
    capturex=int((posx+targetx)/2)
    capturey=int((posy+targety)/2)
    board[capturey][capturex]=0
    return board

def checkPos(board,pos):
    posx=int(ord(pos[0].lower())-97)
    posy=8-int(pos[1])
    if board[posy][posx]==1:
        return True
    else:
        return False
    
def checkMovesWhitePawn(board,pos):
    possibleMoves = set()
    posx=int(ord(pos[0].lower())-97)
    posy=8-int(pos[1])
    if posy>0:
        if posx>0 and board[posy-1][posx-1]==0:
            targetx=chr(posx-1+97)
            targety=8-posy+1
            possibleMoves.add(targetx+str(targety))
        if posx<7 and board[posy-1][posx+1]==0:
            targetx=chr(posx+1+97)
            targety=8-posy+1
            possibleMoves.add(targetx+str(targety))
    return possibleMoves



    