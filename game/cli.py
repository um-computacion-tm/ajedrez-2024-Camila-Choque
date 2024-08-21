from game.chess import Chess

def main():
    chess = Chess()
    while True:
        play(chess)

def play(chess): # El programa solicita al usuario que ingrese la fila y la columna de la pieza que desea mover (from_row, from_col) y la fila y columna de destino (to_row, to_col).
    try:
        # print(chess.show_board())
        print("turn: ", chess.turn)
        from_row = int(input("From row: "))
        from_col = int(input("From col: "))
        to_row = int(input("To Row: "))
        to_col = int(input("To Col: "))
        # :)
        chess.move(
            from_row,
            from_col,
            to_row,
            to_col,
        )
    except Exception as e:
        print("error", e)



