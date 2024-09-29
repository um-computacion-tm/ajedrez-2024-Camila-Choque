
from piezas.piece import Piece
from piezas import direcciones_horse
class Horse(Piece):
    black_str ="♞"  
    white_str ="♘" 
    possible_moves = direcciones_horse
    
    def __init__(self, color):
        super().__init__(color)



    #Verifica los movimientos del caballo
    def movimiento(self,row, col,board):
        moves = []

    #Calcular todos los movimientos
        for move in self.possible_moves:
            new_row = row + move[0]
            new_col = col + move[1]

            #Asegurarse de que el movimiento esté dentro del tablero
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                if not self.pieza_del_mismo_color(new_row,new_col,board):
                     moves.append((new_row, new_col))

        return moves
    
    
    

      
