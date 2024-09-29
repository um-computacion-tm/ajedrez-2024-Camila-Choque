from piezas.piece import Piece



class Pawn(Piece):

    white_str = "♙"
    black_str = "♟"
    def __init__(self, color):
        super().__init__(color)

    #Verifica los movimientos del peon
    def movimiento(self, row, col, board):
        
        es_primer_movimiento = self.__primer_movimiento__
        possibles = []

        #Definir la dirección en función del color
        if self.__color__ == "WHITE":
            direction = -1  #Los peones blancos avanzan hacia filas mayores
        else:  # 'negro'
            direction = 1  #Los peones negros avanzan hacia filas menores

        #Avance de una casilla
        def check_forward(move_distance):
            next_row = row + move_distance * direction
            if 0 <= next_row <= 7 and board.get_piece(next_row, col) is None:  # Solo avanza si la casilla está vacía
                 possibles.append((next_row, col))

    # Avance de una casilla
        check_forward(1)

    # Avance de dos casillas si es el primer movimiento
        if es_primer_movimiento:
            check_forward(2)
        # Verificar capturas en las diagonales
        for delta_col in [-1, 1]:  # Diagonales izquierda (-1) y derecha (+1)
            next_col = col + delta_col
            if 0 <= next_col <= 7:  # Dentro del tablero
              pieza_diagonal = board.get_piece(row + direction, next_col)
              if pieza_diagonal is not None and pieza_diagonal.__color__ != self.__color__:  # Si es una pieza enemiga
                possibles.append((row + direction, next_col))

        return possibles