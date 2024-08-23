from piezas.rook import Rook
from piezas.queen import Queen
from piezas.horse import Horse
from piezas.knight import Knight
from piezas.bishop import Bishop


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
        
        """"
        #POSICIONES REINA    
        self.__positions__[0][3] = Queen("BLACK") 
        self.__positions__[7][3] = Queen("WHITE")
        
        #PISICIONES CABALLOS
        self.__positions__[0][2] = Horse("BLACK") 
        self.__positions__[0][5] = Horse("BLACK") 
        self.__positions__[7][2] = Horse("WHITE") 
        self.__positions__[7][5] = Horse("WHITE") 

        #PISICIONES REY
        self.__positions__[0][4] = Knight("BLACK") 
        self.__positions__[7][4] = Knight("WHITE") 

        #PISICION ALFIL
        self.__positions__[0][1] = Bishop("BLACK") 
        self.__positions__[0][6] = Bishop("BLACK") 
        self.__positions__[7][1] = Bishop("WHITE") 
        self.__positions__[7][6] = Bishop("WHITE") 
        """




    def get_piece(self, row, col):
        return self.__positions__[row][col]