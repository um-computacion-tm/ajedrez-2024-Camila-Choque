from piezas.rook import Rook
from piezas.king import King
from piezas.horse import Horse
from piezas.pawn import Pawn
from piezas.bishop import Bishop
from piezas.queen import Queen
from game.exceptions import OutOfBoard


class Board:
    def __init__(self, for_test=False):
        self.__positions__ = []
        for _ in range(8):
            self.__positions__.append([None] * 8)
        if not for_test:
            #POSICIONES TORRES
            self.__positions__[0][0] = Rook("BLACK") 
            self.__positions__[0][7] = Rook("BLACK") 
            self.__positions__[7][0] = Rook("WHITE") 
            self.__positions__[7][7] = Rook("WHITE") 
            #PISICIONES REY
            self.__positions__[0][4] = King("BLACK") 
            self.__positions__[7][4] = King("WHITE") 
            #POSICIONES CABALLOS
            self.__positions__[0][1] = Horse("BLACK") 
            self.__positions__[0][6] = Horse("BLACK") 
            self.__positions__[7][1] = Horse("WHITE") 
            self.__positions__[7][6] = Horse("WHITE") 
            #PISICION ALFIL
            self.__positions__[0][2] = Bishop("BLACK") 
            self.__positions__[0][5] = Bishop("BLACK") 
            self.__positions__[7][2] = Bishop("WHITE") 
            self.__positions__[7][5] = Bishop("WHITE") 
            #POSICIONES REINA    
            self.__positions__[0][3] = Queen("BLACK") 
            self.__positions__[7][3] = Queen("WHITE")
            #POSICIONES PEONES
            for col in range(8):
                self.__positions__[1][col] = Pawn("BLACK")
                self.__positions__[6][col] = Pawn("WHITE")


        
    #Devuelve la pieza en la posición especificada en el tablero
    def get_piece(self, row, col):
        if 0 <= row < 8 and 0 <= col < 8:
            return self.__positions__[row][col]
        else:
            raise OutOfBoard("Fuera de Rango")
        
    #Genera una representación en cadena del tablero
    def __str__(self):
        board_str = "  0 1 2 3 4 5 6 7\n"  
        for i, row in enumerate(self.__positions__):
            board_str += str(i) + " "  
            for cell in row:
                if cell is not None:
                    board_str += str(cell) + " "  
                else:
                    board_str += ". "  
            board_str += str(i) + "\n"  
        board_str += "  0 1 2 3 4 5 6 7\n"  
        return board_str
    

   #Establece la pieza en la posición especificada del tablero
    def set_piece(self, row, col, piece):
        self.__positions__[row][col] = piece

    #Mueve una pieza desde la posición de origen especificada a la posición de destino
    def move(self, from_row, from_col, to_row, to_col):
        origin = self.get_piece(from_row, from_col)
        self.set_piece(to_row, to_col, origin)
        self.set_piece(from_row, from_col, None)

    #Obtener movimientos validos
    def ver_movimientos_validos(self, row, col):
        piece = self.get_piece(row, col)
        if piece is not None:
            return piece.movimiento(row, col, self)
        else:
            return []
        
        


    
    