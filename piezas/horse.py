
from piezas.piece import Piece
class Horse(Piece):
    black_str ="♘" #knight black
    white_str ="♞"  #knight white
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

    def horse_moves(self,row, col,board):
        moves = []
    # Lista de movimientos posibles en forma de L
        possible_moves = [
          (2, 1), (2, -1),   # Dos hacia arriba, una a la derecha / izquierda
          (-2, 1), (-2, -1), # Dos hacia abajo, una a la derecha / izquierda
          (1, 2), (1, -2),   # Una hacia arriba, dos a la derecha / izquierda
          (-1, 2), (-1, -2)  # Una hacia abajo, dos a la derecha / izquierda
        ] 

    # Calcular todos los movimientos
        for move in possible_moves:
            new_row = row + move[0]
            new_col = col + move[1]

        # Asegurarse de que el movimiento esté dentro del tablero
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                if not self.pieza_del_mismo_color(new_row,new_col,board):
                     moves.append((new_row, new_col))

        return moves
    
    
    

      
