
from piezas.piece import Piece 


class Rook(Piece):
   black_str ="♖"
   white_str ="♜"

   def pieza_del_mismo_color(self, row, col, board):
        #Esta funcion sirve para ver si hay otra pieza del mismo color
        pieza = board[row][col]
        if pieza is not None and pieza.__color__ == self.__color__:
            return True
        else:
            return False
        
   def captura(self, row, col, board):
        #Verifica si la torre puede capturar 
        pieza = board[row][col]
        if pieza is not None and pieza.__color__ != self.__color__:
            return True
        else:
            return False

 

   def posiciones_verticales(self, row, col,board):
        # Verifica los movimientos verticales ascendentes(profe)
        possibles = []
        for next_row in range(row -1, -1, -1): 
            if self.pieza_del_mismo_color(next_row,col,board):
                break
            if self.captura(next_row,col,board):
               possibles.append((next_row, col))
               break
            possibles.append((next_row, col))

        # Verifica los movimientos verticales descendentes(profe)
        for next_row in range(row + 1, 8):
            if self.pieza_del_mismo_color(next_row, col,board):
                break
            if self.captura(next_row,col,board):
                    possibles.append((next_row, col))
                    break
            possibles.append((next_row, col))
        return possibles
       
   def posiciones_horizontales(self, row, col,board):
    #Verifica los movimientos a izquierda de la torre
        possibles = []
        for next_col in range(col - 1, -1, -1):  
            if self.pieza_del_mismo_color((row, next_col,board)):
                break
            if self.captura(row,next_col,board):
                possibles.append((row,next_col))
                break
            possibles.append((row,next_col))

    #Verifica los movimientos a derecha de la torre
        for next_col in range(col + 1, 8):  
            if self.pieza_del_mismo_color((row, next_col,board)):
                break
            if self.captura(row,next_col,board):
                possibles.append((row,next_col))
                break
            possibles.append((row,next_col))
        
        return possibles
   
       


