from mapGen import *
from pawnMove import *
from ai import ai_move
import os


if __name__ == "__main__":

    board = [[0,2,0,2,0,2,0,2],
             [2,0,2,0,2,0,2,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,1,0,1,0,1,0,1],
             [1,0,1,0,1,0,1,0]]


    while True:
        os.system('cls')
        draw(board)
        print()

        if len(checkCaptures())>0:
            pass
        else:
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
        
            