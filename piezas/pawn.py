from piezas.piece import Piece



class Pawn(Piece):
    
  def movimiento_hacia_adelante(self, row, col, es_primer_movimiento, color):
    possibles = []

    # Definir la dirección en función del color
    if color == 'white':
        direction = 1  # Los peones blancos avanzan hacia filas mayores
        fila_inicial = 1
    else:  # 'negro'
        direction = -1  # Los peones negros avanzan hacia filas menores
        fila_inicial = 6

    # Avance de una casilla
    next_row = row + direction 
    if 0 <= next_row <= 7:
        possibles.append((next_row, col))

    # Avance de dos casillas si es el primer movimiento
    if es_primer_movimiento and row == fila_inicial:
        second_row = row + 2 * direction
        if 0 <= second_row <= 7:
            possibles.append((second_row, col))

    return possibles

  
  
