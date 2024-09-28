from piezas.piece import Piece
from piezas.rook import Rook
from piezas.bishop import Bishop


class Queen(Piece):
 black_str ="♛"
 white_str ="♕"
 

 def __init__(self,color):
  self.__bishop__ = Bishop(color)
  self.__rook__ = Rook(color)
  super().__init__(color)

#Valida los movimientos de la reina
 def movimiento(self, row, col, board):
    possibles = []

    # Movimientos diagonales (Alfil)
    possibles += self.__bishop__.movimiento(row, col, board)

    # Movimientos verticales y horizontales (Torre)
    possibles += self.__rook__.movimiento(row, col, board)
    
    return possibles
