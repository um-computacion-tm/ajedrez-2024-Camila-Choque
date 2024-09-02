from piezas.rook import Rook
from piezas.king import King
from piezas.horse import Horse


class Board:
    def __init__(self):
        self.__positions__ = []
        for _ in range(8):
            col = []
            for _ in range(8):
                col.append(None)
            self.__positions__.append(col)
        #POSICIONES TORRES
        self.__positions__[0][0] = Rook("BLACK") # Black
        self.__positions__[0][7] = Rook("BLACK") # Black
        self.__positions__[7][7] = Rook("WHITE") # White
        self.__positions__[7][0] = Rook("WHITE") # White
          #PISICIONES REY
        self.__positions__[0][4] = King("BLACK") 
        self.__positions__[7][4] = King("WHITE") 

        self.__positions__[0][1] = Horse("BLACK") 
        self.__positions__[0][6] = Horse("BLACK") 
        self.__positions__[7][1] = Horse("WHITE") 
        self.__positions__[7][6] = Horse("WHITE") 


        
        
        """"
        #POSICIONES REINA    
        self.__positions__[0][3] = Queen("BLACK") 
        self.__positions__[7][3] = Queen("WHITE")
        
    
        #PISICION ALFIL
        self.__positions__[0][1] = Bishop("BLACK") 
        self.__positions__[0][6] = Bishop("BLACK") 
        self.__positions__[7][1] = Bishop("WHITE") 
        self.__positions__[7][6] = Bishop("WHITE") 
        """
       



    def __str__(self):
        board_str = ""
        for row in self.__positions__:
            for cell in row:
                if cell is not None:
                    board_str += str(cell)
                else:
                    board_str += " "
            board_str += "\n"
        return board_str

    def get_piece(self, row, col):
        return self.__positions__[row][col]

    def set_piece(self, row, col, piece):
        self.__positions__[row][col] = piece