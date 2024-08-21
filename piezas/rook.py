from piezas.piece import Piece 
from game.board import Board


class Rook(Piece):
    def valid_move_rook(self,from_row, from_col, to_row, to_col):
        #MOVMIENTO HORIZONTAL
        if from_row == to_row and from_col != to_col:
            return self.is_clear_path(from_row, from_col, to_row, to_col, Board)
        #MOVIMIENTO VERTICAL
        elif from_col == to_col and from_row != to_row:
            return self.is_clear_path(from_row, from_col, to_row, to_col, Board)
        return False
    
    
        


