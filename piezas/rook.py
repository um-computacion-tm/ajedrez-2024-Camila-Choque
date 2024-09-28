
from piezas.piece import Piece 


class Rook(Piece):
   black_str ="♜"
   white_str ="♖"
  

   def __init__(self, color):
        super().__init__(color)

   #Verifica los movimientos de la torre
   def movimiento(self, row, col, board):
       possibles = []

    #Movimientos verticales hacia arriba
       for next_row in range(row - 1, -1, -1):
        if self.pieza_del_mismo_color(next_row, col, board):
            break
        if self.captura(next_row, col, board):
            possibles.append((next_row, col))
            break
        possibles.append((next_row, col))

    #Movimientos verticales hacia abajo
       for next_row in range(row + 1, 8):
        if  self.pieza_del_mismo_color(next_row, col, board):
            break
        if  self.captura(next_row, col, board):
            possibles.append((next_row, col))
            break
        possibles.append((next_row, col))

    #Movimientos horizontales hacia la izquierda
       for next_col in range(col - 1, -1, -1):
         if self.pieza_del_mismo_color(row, next_col, board):
            break
         if self.captura(row, next_col, board):
            possibles.append((row, next_col))
            break
         possibles.append((row, next_col))

    #Movimientos horizontales hacia la derecha
       for next_col in range(col + 1, 8):
         if self.pieza_del_mismo_color(row, next_col, board):
            break
         if self.captura(row, next_col, board):
            possibles.append((row, next_col))
            break
         possibles.append((row, next_col))

    #Ordenar las posiciones para asegurar el orden correcto
       possibles.sort()
       return possibles
   
 

   
   
   

