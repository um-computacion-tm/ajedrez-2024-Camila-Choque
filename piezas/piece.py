class Piece:    
    def __init__(self, color):
        self.__color__ = color
        self.__primer_movimiento__ = True
        
    
    def get_color(self):
        return self.__color__

    def __str__(self):
        if self.__color__ == "WHITE":
            return self.white_str
        else:
            return self.black_str

    #Esta funcion sirve para ver si hay otra pieza del mismo color
    def pieza_del_mismo_color(self, row, col, board):
        pieza = board.get_piece(row,col)
        if pieza is not None and pieza.__color__ == self.__color__:
            return True
        else:
            return False
    #Verifica si puede capturar  
    def captura(self, row, col, board):
        pieza = board.get_piece(row,col)
        if pieza is not None and pieza.__color__ != self.__color__:
            return True
        else:
            return False

   
    
   

    """"
    def control(self, row, col, board):
        return self.movimientos_horizontales_y_verticales(row, col,board)
    
    """
    
   
   

    