from mapGen import *
from pawnMove import *
from ai import Ai
import os
from end import checkWin


if __name__ == "__main__":

    board = [[0,2,0,2,0,2,0,2],
             [2,0,2,0,2,0,2,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,1,0,1,0,1,0,1],
             [1,0,1,0,1,0,1,0]]
    # board = [[0,0,0,2,0,0,0,0],
            #  [0,0,0,0,0,0,2,0],
            #  [0,0,0,0,0,1,0,0],
            #  [2,0,0,0,1,0,2,0],
            #  [0,0,0,0,0,0,0,1],
            #  [1,0,0,0,0,0,0,0],
            #  [0,0,0,0,0,0,0,0],
            #  [0,0,1,0,0,0,4,0]]


    while True:
        caputuredThisTurn=False
        if len(checkCaptures(board))>0:
            os.system('cls')
            draw(board)
            print()
            pos=input("Enter pawn fieldX: ")
            capturingPawns = []
            capturePos = []
            moreCaptures=True
            for i in checkCaptures(board):
                capturingPawns.append(i[0])
                capturePos.append(i[1])
            while checkPos(board,pos)==False or pos.lower() not in capturingPawns:
                print("There is possible capture with pawn on another field!")
                pos=input("Enter pawn field: ")
                possibleMoves = checkMovesWhitePawn(board,pos)
            capturesForPawn = []
            for i in range(len(capturePos)):
                if capturingPawns[i]==pos:
                    capturesForPawn.append(capturePos[i])
            target=input("Enter where do you want pawn to move: ")
            while target.lower()not in capturesForPawn:
                print("Incorrect field!")
                target=input("Enter where do you want pawn to move: ")
            board = capture(board,pos,target)
            board = move(board,pos,target)
            board = checkPromotions(board)
            
            caputuredThisTurn=True
            pos=target
            while len(checkCaptures(board))>0 and moreCaptures==True:   
                os.system('cls')
                draw(board)
                print()
                capturingPawns=[]
                capturePos=[]
                capturesForPawn=[]
                newCaptures = list(checkCaptures(board))

                for i in range(len(newCaptures)):
                    capturingPawns.append(newCaptures[i][0])
                    capturePos.append(newCaptures[i][1])
                for i in range(len(capturePos)):
                    if capturingPawns[i]==pos:
                        capturesForPawn.append(capturePos[i])
                if len(capturesForPawn)>0:
                    target=input("Enter where do you want pawn to move: ")
                    while target.lower() not in capturesForPawn:
                        print("Incorrect field!")
                        target=input("Enter where do you want pawn to move: ")
                    board = capture(board,pos,target)
                    board = move(board,pos,target)
                    board = checkPromotions(board)
                    pos=target
                else:
                    moreCaptures=False
        else: 
            if caputuredThisTurn==False:
                os.system('cls')
                draw(board)
                print()
                pos=input("Enter pawn field: ")
                possibleMoves = checkMovesWhitePawn(board,pos)
                while checkPos(board,pos)==False or len(possibleMoves)==0:
                    print("There is no pawn on chosen field that you could move!")
                    pos=input("Enter pawn field: ")
                    possibleMoves = checkMovesWhitePawn(board,pos)
                target=input("Enter where do you want pawn to move: ")
                while target.lower()not in(possibleMoves):
                    if target.lower() == "back":
                        pos=input("Enter pawn field: ")
                        possibleMoves = checkMovesWhitePawn(board,pos)
                        while checkPos(board,pos)==False or len(possibleMoves)==0:
                            print("There is no pawn on chosen field that you could move!")
                            pos=input("Enter pawn field: ")
                            possibleMoves = checkMovesWhitePawn(board,pos)
                    else:
                        print("Incorrect field! (type 'back' to choose other pawn)")
                    target=input("Enter where do you want pawn to move: ")
                board = move(board,pos,target)
                board = checkPromotions(board)
        os.system('cls')
        draw(board)
        if checkWin(board)!=False:
                os.system('cls')
                draw(board)
                if checkWin(board)==1:
                    print("Congratulations, you won!")
                else:
                    print("Shame on you, you lost!")
                break
        board = Ai(board)
        if checkWin(board)!=False:
                os.system('cls')
                draw(board)
                if checkWin(board)==1:
                    print("Congratulations, you won!")
                else:
                    print("Shame on you, you lost!")
                break
        
        #input("confirm end of turn")
        
            