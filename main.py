from mapGen import *
from pawnMove import *
from ai import ai_move
import os


if __name__ == "__main__":

    # board = [[0,2,0,2,0,2,0,2],
            #  [2,0,2,0,2,0,2,0],
            #  [0,0,0,0,0,0,0,0],
            #  [0,0,0,0,0,0,0,0],
            #  [0,0,0,0,0,0,0,0],
            #  [0,0,0,0,0,0,0,0],
            #  [0,1,0,1,0,1,0,1],
            #  [1,0,1,0,1,0,1,0]]
    board = [[0,2,0,2,0,2,0,2],
             [0,0,0,0,2,0,2,0],
             [0,2,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,2,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,1,0,1,0,1,0,1],
             [1,0,1,0,1,0,1,0]]


    while True:
        caputuredThisTurn=False
        while len(checkCaptures(board))>0:
            os.system('cls')
            draw(board)
            print()
            pos=input("Podaj pole pionkaX: ")
            capturingPawns = []
            capturePos = []
            for i in checkCaptures(board):
                capturingPawns.append(i[0])
                capturePos.append(i[1])
            while checkPos(board,pos)==False or pos.lower() not in capturingPawns:
                print("Aktualnie mozlwie jest bicie przy pomocy pionka na innym polu!")
                pos=input("Podaj pole pionka: ")
                possibleMoves = checkMovesWhitePawn(board,pos)
            capturesForPawn = []
            for i in range(len(capturePos)):
                if capturingPawns[i]==pos:
                    capturesForPawn.append(capturePos[i])
            #print(capturesForPawn)
            target=input("Podaj gdzie go chcesz ruszyc pionka: ")
            while target.lower()not in capturesForPawn:
                print("Podano nieprawidlowe pole!")
                target=input("Podaj gdzie go chcesz ruszyc pionka: ")
            board = capture(board,pos,target)
            board = move(board,pos,target)
            caputuredThisTurn=True
        else: 
            if caputuredThisTurn==False:
                os.system('cls')
                draw(board)
                print()
                pos=input("Podaj pole pionka: ")
                possibleMoves = checkMovesWhitePawn(board,pos)
                while checkPos(board,pos)==False or len(possibleMoves)==0:
                    print("Na podanym polu nie znajduje sie pionek ktorym mozes sie ruszyc!")
                    pos=input("Podaj pole pionka: ")
                    possibleMoves = checkMovesWhitePawn(board,pos)
                target=input("Podaj gdzie go chcesz ruszyc pionka: ")
                while target.lower()not in(possibleMoves):
                    print("Podano nieprawidlowe pole!")
                    target=input("Podaj gdzie go chcesz ruszyc pionka: ")
                board = move(board,pos,target)
                ai_move(board)
        #input("confirm end of turn")
        
            