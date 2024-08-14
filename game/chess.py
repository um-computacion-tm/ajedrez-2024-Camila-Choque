from board import Board

class Chess():
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "white"  #Este atributo rastrea de quién es el turno para mover una pieza.
                                 #Se inicializa como "white", indicando que las blancas tienen el primer turno.

    def move(self, from_row, from_col, to_row, to_col):  #from_row, from_col: La posición inicial de la pieza que se quiere mover.
                                                         #to_row, to_col: La posición a la que se quiere mover la pieza.
        pass

        #validate coords
        piece = self.board.get_piece(from_row, from_col)
        self.change_turn()

    def change_turn(self): #Alterna el turno de los jugadores
        if self.__turn__ == "WHITE":
            self.__turn__ = "BLACK"
        else:
            self.__turn__ = "WHITE"

    def show_board(self): #muestra el tablero de forma actualizada 
        pass