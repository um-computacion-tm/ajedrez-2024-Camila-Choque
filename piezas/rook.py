from piezas.piece import Piece 



class Rook(Piece):
     def valid_move_rook(self, current_position, new_position):
        # Coordenadas actuales y nuevas
        x1, y1 = current_position
        x2, y2 = new_position

        # Verifica si el movimiento es horizontal o vertical
        if x1 == x2 or y1 == y2:
            # Verifica que la nueva posición está dentro del rango del tablero
            if 1 <= x2 <= 8 and 1 <= y2 <= 8:
                return True
        return False



    
        


