from piece import Piece
from game.board import Board

class Queen(Piece):

 def __init__(self,movimiento):
  self.nombre = Queen
  self.movimiento = movimiento

def valid_move_queen(self, from_row, from_col, to_row, to_col):
   #MOVIMIENTO HORIZONTAL
   if from_row == to_row and from_col != to_col:
            return self.is_clear_path(from_row, from_col, to_row, to_col, Board)
   
   #MOVIMIENTO VERTICAL
   elif from_col == to_col and from_row != to_row:
       return self.is_clear_path((from_row, from_col, to_row, to_col, Board))
   
   # Movimiento diagonal
   elif abs(from_row - to_row) == abs(from_col - to_col):
        return self.is_clear_path(from_row, from_col, to_row, to_col, Board)
  
   return False