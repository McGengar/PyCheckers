from mapGen import *
from pawnMove import *
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
        pos=input("Podaj pole pionka: ")
        target=input("Podaj gdzie go chcesz ruszyc pionka: ")
        board = move(board,pos,target)
        
            