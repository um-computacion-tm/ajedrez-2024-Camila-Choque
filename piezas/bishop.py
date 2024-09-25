from piezas.piece import Piece

class Bishop(Piece):
   black_str ="♗"
   white_str ="♝"
   def __init__(self, color):
        super().__init__(color)
        
        

   def pieza_del_mismo_color(self, row, col, board):
        #Esta funcion sirve para ver si hay otra pieza del mismo color
        pieza = board.get_piece(row,col)
        if pieza is not None and pieza.__color__ == self.__color__:
            return True
        else:
            return False
        
   def captura(self, row, col, board):
        #Verifica si la torre puede capturar 
        pieza = board.get_piece(row,col)
        if pieza is not None and pieza.__color__ != self.__color__:
            return True
        else:
            return False

     #VERIFICA LOS MOVIMIENTOS DIAGONALES   
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