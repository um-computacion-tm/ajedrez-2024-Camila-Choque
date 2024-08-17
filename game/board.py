from piece.rook import Rook
from piece.queen import Queen


class Board:
    def __init__(self):
        self.__positions__ = []
        for _ in range(8):
            col = []
            for _ in range(8):
                col.append(None)
            self.__positions__.append(col)
        #POSICIONES TORRES
        self.__positions__[0][0] = Rook("BLACK") 
        self.__positions__[0][7] = Rook("BLACK") 
        self.__positions__[7][7] = Rook("WHITE") 
        self.__positions__[7][0] = Rook("WHITE") 

        #POSICIONES REINA    
        self.__positions__[0][3] = Queen("BLACK") 
        self.__positions__[7][3] = Queen("WHITE")


    def get_piece(self, row, col):
        return self.__positions__[row][col]