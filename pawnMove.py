
def move(board, pos, target):
    posx=int(ord(pos[0].lower())-97)
    posy=8-int(pos[1])
    targetx=int(ord(target[0].lower())-97)
    targety=8-int(target[1])
    pawn = board[posy][posx]
    board[posy][posx]=0
    board[targety][targetx]=pawn
    return board
