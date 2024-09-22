from piezas.piece import Piece



class Pawn(Piece):
  
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
    
  def movimiento_hacia_adelante(self, row, col, es_primer_movimiento, color, board):
    possibles = []

    # Definir la dirección en función del color
    if color == 'white':
        direction = 1  # Los peones blancos avanzan hacia filas mayores
    else:  # 'negro'
        direction = -1  # Los peones negros avanzan hacia filas menores

    # Avance de una casilla
    next_row = row + direction
    if 0 <= next_row <= 7 and board.get_piece(next_row, col) is None:  # Solo avanza si la casilla está vacía
        possibles.append((next_row, col))

    # Avance de dos casillas si es el primer movimiento
    if es_primer_movimiento and board.get_piece(next_row, col) is None:
        second_row = row + 2 * direction
        if 0 <= second_row <= 7 and board.get_piece(second_row, col) is None:
            possibles.append((second_row, col))

    # Verificar capturas en las diagonales
    for delta_col in [-1, 1]:  # Diagonales izquierda (-1) y derecha (+1)
        next_col = col + delta_col
        if 0 <= next_col <= 7:  # Dentro del tablero
            pieza_diagonal = board.get_piece(next_row, next_col)
            if pieza_diagonal is not None and pieza_diagonal.color != color:  # Si es una pieza enemiga
                possibles.append((next_row, next_col))

    return possibles

  
