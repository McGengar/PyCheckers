def checkWin(board):
    black = 0
    white = 0
    count = []
    for i,row in enumerate(board):
        for index,column in enumerate(row):
            if column==1 or column==3:
                white+=1
            if column==2 or column==4:
                black+=1
    if white == 0:
        return 2
    elif black == 0:
        return 1
    else: return False
    