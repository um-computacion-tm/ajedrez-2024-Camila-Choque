
from piezas.piece import Piece 


class Rook(Piece):
   black_str ="♖"
   white_str ="♜"
   
   def possible_position_vd(self,row,col):
        possibles = []
        for next_row in range(row +1, 8): #range(inicio, fin que no esta incluido)
            possibles.append((next_row, col))
        return possibles
    
   def possible_positions_va(self, row, col):
        possibles = []
        for next_row in range(row -1, -1, -1): #range(inicio, fin que no esta incluido)
            possibles.append((next_row, col))
        return possibles    