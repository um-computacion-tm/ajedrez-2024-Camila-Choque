from piezas.piece import Piece


class Pawn(Piece):
    

    def movimiento_hacia_adelante(self, from_pos, to_pos, direccion, board):
        from_row, from_col = from_pos
        to_row, to_col = to_pos
        pieza_destino = board.get_piece(to_row, to_col)
        return (from_col == to_col and 
                to_row == from_row + direccion and 
                pieza_destino is None)

   