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
        

    def movimiento(self, row, col, board):
        possibles = []
        # Direcciones diagonales: arriba-derecha, arriba-izquierda, abajo-derecha, abajo-izquierda
        

        for dr, dc in self.direcciones:
            r, c = row + dr, col + dc
            while 0 <= r < 8 and 0 <= c < 8:
                if self.pieza_del_mismo_color(r, c, board):
                    break
                if self.captura(r, c, board):
                    possibles.append((r, c))
                    break
                possibles.append((r, c))
                r += dr
                c += dc

        return possibles
   
    
   

    """"
    def control(self, row, col, board):
        return self.movimientos_horizontales_y_verticales(row, col,board)
    
    """
    
   
   

    