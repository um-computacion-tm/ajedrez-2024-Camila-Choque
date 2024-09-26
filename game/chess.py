from game.board import Board
from game.exceptions import InvalidMove
from game.exceptions import InvalidTurn
from game.exceptions import EmptyPosition

class Chess():
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "WHITE"  #Este atributo rastrea de quién es el turno para mover una pieza.
                                 #Se inicializa como "white", indicando que las blancas tienen el primer turno.

    def change_turn(self): #Alterna el turno de los jugadores
        if self.__turn__ == "WHITE":
            self.__turn__ = "BLACK"
        else:
            self.__turn__ = "WHITE"

    def is_playing(self):
        return True
    def show_board(self):
        return str(self.__board__)
    @property
    def turn(self):
        return self.__turn__

    
    def fin(self):
        self.playing = False  
        print("Fin de la Partida.")

    def validar(self, from_row, from_col, to_row, to_col):
        #from_row, from_col: La posición inicial de la pieza que se quiere mover.
        #to_row, to_col: La posición a la que se quiere mover la pieza.
        comienzo = self.__board__.get_piece(from_row, from_col)
        if comienzo is None:
            raise EmptyPosition("Casilla vacia.")
        if comienzo.__color__ != self.__turn__:
            raise InvalidTurn(f"Turno de: {self.__turn__}")
        movimientos = comienzo.movimientos(from_row, from_col, self.__board__)
        if (to_row, to_col) not in movimientos:
            raise InvalidMove("Movimiento Invalido.")
        self.__board__.set_piece(to_row, to_col, comienzo)
        self.__board__.set_piece(from_row, from_col, None)
        self.change_turn()


   
        
          