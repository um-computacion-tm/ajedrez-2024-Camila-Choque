from piezas.piece import Piece
class King(Piece):
    black_str ="♔"
    white_str ="♚"
    def __init__(self, color):
        super().__init__(color)
    def valid_move_king(self,from_row,from_col):

        nuevos_movimientos = []
        direcciones = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        for direccion in direcciones:
            r, c = from_row + direccion[0], from_col + direccion[1]
            if 0 <= r < 8 and 0 <= c < 8:
             nuevos_movimientos.append((r,c))
        return nuevos_movimientos
    
    