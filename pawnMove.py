
def move(board, pos, target):
    posx=int(ord(pos[0].lower())-97)
    posy=8-int(pos[1])
    targetx=int(ord(target[0].lower())-97)
    targety=8-int(target[1])
    pawn = board[posy][posx]
    board[posy][posx]=0
    board[targety][targetx]=pawn
    return board

def checkCaptures():
    pass

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
    #print(posx,posy)
    if posy>0:
        if posx>0 and board[posy-1][posx-1]==0:
            targetx=chr(posx-1+97)
            targety=8-posy+1
            #print(posx-1,posy-1)
            possibleMoves.add(targetx+str(targety))
        if posx<7 and board[posy-1][posx+1]==0:
            targetx=chr(posx+1+97)
            targety=8-posy+1
            #print(posx+1,posy-1)
            possibleMoves.add(targetx+str(targety))
    #print(possibleMoves)
    return possibleMoves



    