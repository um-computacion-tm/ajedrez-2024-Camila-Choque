
from piezas.piece import Piece 


class Rook(Piece):
   black_str ="♖"
   white_str ="♜"

   def possible_positions_vd(self, row, col, board):
        possibles = []
        for next_row in range(row + 1, 8):
            other_piece = board.get_piece(next_row, col)
            if other_piece is not None:
                # Si hay una pieza y es del mismo color, romper el bucle
                if other_piece.__color__ == self.__color__:
                    break
                # Si hay una pieza y es de un color diferente, agregar el movimiento y romper el bucle
                if other_piece.__color__ != self.__color__:
                    possibles.append((next_row, col))
                    break
            # Si no hay una pieza, agregar el movimiento
            possibles.append((next_row, col))
        return possibles
 

        
""""
   def possible_positions_va(self, row, col):
        possibles = []
        for next_row in range(row -1, -1, -1): 
            possibles.append((next_row, col))
        return possibles    
   

   def possible_positions_derecha(self, row, col):
    possibles = []
    for next_col in range(col + 1, 8):  
        possibles.append((row, next_col))
    return possibles
   
   def possible_positions_izquierda(self, row, col):
    possibles = []
    for next_col in range(col - 1, -1, -1):  
        possibles.append((row, next_col))
    return possibles

    #ARREGLARRRRRRRRRRRRRR
   def captura(self, row, col, board):
        captures = []
        
        # Verificar en vertical hacia abajo
        for next_row in range(row + 1, 8):
            piece = board.get_piece_at((next_row, col))
            if piece is None:
                continue
            if piece.color != self.color:
                captures.append((next_row, col))
                break  
            else:
                break  
        
        # Verificar en vertical hacia arriba
        for next_row in range(row - 1, -1, -1):
            piece = board.get_piece_at((next_row, col))
            if piece is None:
                continue
            if piece.color != self.color:
                captures.append((next_row, col))
                break 
            else:
                break  
        
        # Verificar hacia la derecha
        for next_col in range(col + 1, 8):
            piece = board.get_piece_at((row, next_col))
            if piece is None:
                continue
            if piece.color != self.color:
                captures.append((row, next_col))
                break 
            else:
                break  #
        
        # Verificar hacia la izquierda
        for next_col in range(col - 1, -1, -1):
            piece = board.get_piece_at((row, next_col))
            if piece is None:
                continue
            if piece.color != self.color:
                captures.append((row, next_col))
                break  
            else:
                break  
        return captures
    """
