from game.chess import Chess
from game.exceptions import InvalidMove, InvalidTurn, EmptyPosition

def main():

    chess = Chess()
    while chess.is_playing:
        play(chess)

def play(chess):
    try:

        print("      ")
        print("      ")
        print("-------------------------------¡VAMOS A COMENZAR!------------------------------------------------")
        print("-------------------------------------------------------------------------------------------------")
        print("----------------------------------Mucha Suerte---------------------------------------------------")
        print("      ")
        print(chess.show_board())
        print("Turno: ", chess.turn)
        print("-----MENU----")
        print("Blancas:♘")
        print("Negras:♞")
        menu = input("1. Mover pieza\n2. Cancelar Partida\nElija una opción: ")
        if menu == "1":
            
            from_row = int(input("Fila de la pieza que desea mover: "))
            from_col = int(input("Columan de la pieza que desa mover: "))
            to_row = int(input("Fila destino: "))
            to_col = int(input("Columna destino: "))

            chess.validar(from_row, from_col, to_row, to_col)
            
          
        elif menu == "2":
            chess.fin()
            return
        else:
            print("Opción inválida")

    except InvalidTurn as e:
        print(e)

    except EmptyPosition as e:
        print(e)

    except InvalidMove as e:
        print(e)

    except Exception as e:
        print("error", e)

if __name__ == '__main__':
      main()
