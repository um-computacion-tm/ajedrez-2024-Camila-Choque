class Piece:    
    def __init__(self, color):
        self.__color__ = color
        
    
    def get_color(self):
        return self.__color__

    def __str__(self):
        if self.__color__ == "WHITE":
            return self.white_str
        else:
            return self.black_str

        
    def pieza_del_mismo_color(self, row, col, board):
        #Esta funcion sirve para ver si hay otra pieza del mismo color
        pieza = board.get_piece(row,col)
        if pieza is not None and pieza.__color__ == self.__color__:
            return True
        else:
            return False
        
    def captura(self, row, col, board):
        #Verifica si puede capturar 
        pieza = board.get_piece(row,col)
        if pieza is not None and pieza.__color__ != self.__color__:
            return True
        else:
            return False

    def movimientos_horizontales_y_verticales(self, row, col, board):
       possibles = []

    # Movimientos verticales hacia arriba
       for next_row in range(row - 1, -1, -1):
        if self.pieza_del_mismo_color(next_row, col, board):
            break
        if self.captura(next_row, col, board):
            possibles.append((next_row, col))
            break
        possibles.append((next_row, col))

    # Movimientos verticales hacia abajo
       for next_row in range(row + 1, 8):
        if  self.pieza_del_mismo_color(next_row, col, board):
            break
        if  self.captura(next_row, col, board):
            possibles.append((next_row, col))
            break
        possibles.append((next_row, col))

    # Movimientos horizontales hacia la izquierda
       for next_col in range(col - 1, -1, -1):
         if self.pieza_del_mismo_color(row, next_col, board):
            break
         if self.captura(row, next_col, board):
            possibles.append((row, next_col))
            break
         possibles.append((row, next_col))

    # Movimientos horizontales hacia la derecha
       for next_col in range(col + 1, 8):
         if self.pieza_del_mismo_color(row, next_col, board):
            break
         if self.captura(row, next_col, board):
            possibles.append((row, next_col))
            break
         possibles.append((row, next_col))

    # Ordenar las posiciones para asegurar el orden correcto
       possibles.sort()
       return possibles
    def control(self, row, col, board):
        return self.movimientos_horizontales_y_verticales(row, col, board)
    
    
   
   

    