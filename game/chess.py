from game.board import Board
from game.exceptions import InvalidMove
from game.exceptions import InvalidTurn
from game.exceptions import EmptyPosition
from piezas.king import King

class Chess():
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "WHITE"
        
                                #Este atributo rastrea de quién es el turno para mover una pieza.
       
                                 #Se inicializa como "white", indicando que las blancas tienen el primer turno.
    #Alterna el turno de los jugadores
    def change_turn(self): 
        if self.__turn__ == "WHITE":
            self.__turn__ = "BLACK"
        else:
            self.__turn__ = "WHITE"
    #Da comienzo a la partida
    def is_playing(self):
        return True
    #Muestra el tablero
    def show_board(self):
        return str(self.__board__)
    #Devuelve el turno
    @property
    def turn(self):
        return self.__turn__

    #Termina la partida
    def fin(self):
        self.playing = False  
        print("Fin de la Partida.")

    #Valida los todos los movimientos
    def validar(self, from_row, from_col, to_row, to_col):
        # Obtener la pieza de la posición de origen desde el tablero
        origin = self.__board__.get_piece(from_row, from_col)
        # Verificar que la pieza existe
        if origin is None:
            raise EmptyPosition("Ninguna pieza en la posición inicial.")
        # Verificar que la pieza es del turno actual
        if origin.__color__ != self.__turn__:
            raise InvalidTurn(f"Es el turno de {self.__turn__}")
        # Obtener los movimientos válidos de la pieza en la posición actual
        control = origin.movimiento(from_row, from_col, self.__board__)
        # Verificar si el movimiento está en los movimientos válidos
        if (to_row, to_col) not in control:
            raise InvalidMove("Movimiento no válido para la pieza.")
        # Realizar el movimiento si es válido
        self.__board__.set_piece(to_row, to_col, origin)
        self.__board__.set_piece(from_row, from_col, None)
        origin.__primer_movimiento__ = False
        self.check_kings()
        self.change_turn()


    def check_kings(self):
        white_king_present = False
        black_king_present = False

        for row in range(8):
            for col in range(8):
                piece = self.__board__.get_piece(row, col)
                if isinstance(piece, King):
                    if piece.__color__ == "WHITE":
                        white_king_present = True
                    elif piece.__color__ == "BLACK":
                        black_king_present = True

        if not white_king_present or not black_king_present:
            winner = "WHITE" if white_king_present else "BLACK"
            self.fin_ganador(winner)
            return winner  
        return None  

    
    def fin_ganador(self, winner):
        self.is_playing = False
        print(f"Fin de la Partida. El ganador es: {winner}")

