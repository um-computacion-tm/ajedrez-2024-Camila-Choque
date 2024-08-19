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

def is_clear_path(self, from_row, from_col, to_row, to_col, board):
        # Chequeo para ver si hay obstáculos en el camino
        row_step = 1 if to_row > from_row else -1 if to_row < from_row else 0
        col_step = 1 if to_col > from_col else -1 if to_col < from_col else 0

        current_row = from_row + row_step
        current_col = from_col + col_step

        while current_row != to_row or current_col != to_col:
            if board.get_piece(current_row, current_col) is not None:
                return False
            current_row += row_step
            current_col += col_step

        return True