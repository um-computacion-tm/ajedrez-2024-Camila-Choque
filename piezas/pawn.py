from piezas.piece import Piece


class Pawn(Piece):
    

    def movimiento_hacia_adelante(self, from_pos, to_pos, direccion, board):
        from_row, from_col = from_pos
        to_row, to_col = to_pos
        pieza_destino = board.get_piece(to_row, to_col)
        return (from_col == to_col and 
                to_row == from_row + direccion and 
                pieza_destino is None)
    
    def inicio_doble_(self, from_pos, to_pos, direccion, board):
        from_row, from_col = from_pos
        to_row, to_col = to_pos
        pieza_destino = board.get_piece(to_row, to_col)
        es_movimiento_valido = (
            (self.get_color() == "White" and from_row == 6) or 
            (self.get_color() == "Black" and from_row == 1)
        )
        return (es_movimiento_valido and 
                to_row == from_row + 2 * direccion and 
                pieza_destino is None and 
                board.get_piece(from_row + direccion, from_col) is None)
    
    