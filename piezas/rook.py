
from piezas.piece import Piece 


class Rook(Piece):
   black_str ="♖"
   white_str ="♜"
   
   def possible_positions_vd(self,row,col):
        possibles = []
        for next_row in range(row +1, 8): 
            possibles.append((next_row, col))
        return possibles
    
   def possible_positions_va(self, row, col):
        possibles = []
        for next_row in range(row -1, -1, -1): 
            possibles.append((next_row, col))
        return possibles    
   

   #ARREGLARRRRRRRRRRRRRRRRRRRRRRR
   def possible_positions_d(self, row, col):
    possibles = []
    for next_col in range(col + 1, 8):  
        possibles.append((row, next_col))
    return possibles
   
   def possible_positions_i(self, row, col):
    possibles = []
    for next_col in range(col - 1, -1, -1):  
        possibles.append((row, next_col))
    return possibles

