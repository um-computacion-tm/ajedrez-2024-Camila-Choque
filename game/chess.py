from game.board import Board
from game.exceptions import InvalidMove
from game.exceptions import InvalidTurn
from game.exceptions import EmptyPosition

class Chess():
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "WHITE"  #Este atributo rastrea de quién es el turno para mover una pieza.
       
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

        # Cambiar el turno después de un movimiento exitoso
        self.change_turn()
""""
    def partida_terminada( piezas_blancas, piezas_negras):
    
    # Verificar si el rey blanco ha sido capturado
        rey_blanco_capturado = not any(pieza == 'KING' for pieza in piezas_blancas)

    # Verificar si el rey negro ha sido capturado
        rey_negro_capturado = not any(pieza == 'KING' for pieza in piezas_negras)

    # Verificar si no hay piezas blancas
        no_piezas_blancas = len(piezas_blancas) == 0

    # Verificar si no hay piezas negras
        no_piezas_negras = len(piezas_negras) == 0

    # La partida termina si alguna de las condiciones se cumple
        return rey_blanco_capturado or rey_negro_capturado or no_piezas_blancas or no_piezas_negras

"""


   
        
          