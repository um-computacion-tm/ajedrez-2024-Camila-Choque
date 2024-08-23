from piezas.piece import Piece 



class Rook(Piece):
     def valid_move_rook(self):
          
          movimientos_nuevos = []
          direcciones = [(1, 0), (-1, 0), (0, 1), (0, -1)]
          for movimientos in direcciones:
               row = x
               col = y
               while True:
                    x += movimientos[row]
                    y += movimientos[col]
                    if 1 <= x <= 8 and 1 <= y <= 8:
                     movimientos_nuevos.append((x, y))
               else:
                    break
          return movimientos_nuevos

                