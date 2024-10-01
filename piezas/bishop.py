from piezas.piece import Piece
from piezas import direcciones_alfil

class Bishop(Piece):
   white_str = "♗"
   black_str = "♝"
   direcciones = direcciones_alfil

    #Veridica los movimientos diagonales
  