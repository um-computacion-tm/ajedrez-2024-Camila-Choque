from piezas.piece import Piece
from piezas import direcciones_alfil

class Bishop(Piece):
   white_str = "♗"
   black_str = "♝"
   direcciones = direcciones_alfil
   def __init__(self, color):
        super().__init__(color)
        
    

    #Veridica los movimientos diagonales
  