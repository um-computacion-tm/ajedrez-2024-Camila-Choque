from piezas.piece import Piece
class King(Piece):
    black_str ="♔"
    white_str ="♚"
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
        
   
    def valid_move_king(self, from_row, from_col, board):
        nuevos_movimientos = []
        direcciones = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        for direccion in direcciones:
            r, c = from_row + direccion[0], from_col + direccion[1]
            if 0 <= r < 8 and 0 <= c < 8:
                if not self.pieza_del_mismo_color(r, c, board):
                    if self.captura(r, c, board):
                       nuevos_movimientos.append((r, c))
                    else:
                        nuevos_movimientos.append((r, c))
        return nuevos_movimientos

    
     