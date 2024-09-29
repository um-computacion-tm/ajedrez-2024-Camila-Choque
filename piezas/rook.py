
from piezas.piece import Piece 
from piezas import direcciones_torre


class Rook(Piece):
   black_str ="♜"
   white_str ="♖"
   direcciones = direcciones_torre
  

   def __init__(self, color):
        super().__init__(color)

   #Verifica los movimientos de la torre
   def movimiento(self, row, col, board):
        moves = []
        for direc_row, direc_col in self.direcciones:
            r, c = row + direc_row, col + direc_col
            while 0 <= r < 8 and 0 <= c < 8:
                if self.pieza_del_mismo_color(r, c, board):
                    break
                if self.captura(r, c, board):
                    moves.append((r, c))
                    break
                moves.append((r, c))
                r += direc_row
                c += direc_col
        return moves
 

   
   
   

