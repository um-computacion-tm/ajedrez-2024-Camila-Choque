from piezas.piece import Piece

class Bishop(Piece):
   white_str = "♗"
   black_str = "♝"
   def __init__(self, color):
        super().__init__(color)
        
    

    #Veridica los movimientos diagonales
   def movimiento(self, row, col, board):
        possibles = []
        # Direcciones diagonales: arriba-derecha, arriba-izquierda, abajo-derecha, abajo-izquierda
        directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

        for dr, dc in directions:
            r, c = row + dr, col + dc
            while 0 <= r < 8 and 0 <= c < 8:
                if self.pieza_del_mismo_color(r, c, board):
                    break
                if self.captura(r, c, board):
                    possibles.append((r, c))
                    break
                possibles.append((r, c))
                r += dr
                c += dc

        return possibles