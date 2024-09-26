import unittest
from game.chess import Chess
from game.board import Board
from game.exceptions import InvalidMove
from game.exceptions import InvalidTurn
from game.exceptions import EmptyPosition

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.chess = Chess()
        self.board = Board()
        self.board = Board(for_test=True)

       
    def test_is_playing(self):
        self.assertTrue(self.chess.is_playing())

    def test_turn(self):
        self.assertEqual(self.chess.turn, "WHITE")

    def test_change_turn(self):
    # Verifca el turno inicial debería ser WHITE
     self.assertEqual(self.chess.turn, "WHITE")
    # Cambia el turno
     self.chess.change_turn()
    # Verifica que el turno ahora es BLACK
     self.assertEqual(self.chess.turn, "BLACK")
    # Cambia el turno de nuevo
     self.chess.change_turn()
    # Verifica que el turno vuelve a ser WHITE
     self.assertEqual(self.chess.turn, "WHITE")

    def test_fin(self):
        # Llama al método fin
        self.chess.fin()
        # Asegura de que el turno sea "WHITE" después de finalizar 
        self.assertEqual(self.chess.turn, "WHITE")
        # Comprobar que el estado de juego se ha cambiado a False 
        self.assertFalse(self.chess.playing)
        # Verifica que el tablero mostrado sea igual al tablero inicial
        self.assertEqual(str(self.chess.show_board()), str(Board()))

    def test_validar_mover_pieza_vacia(self):
        # Intenta mover de una posición vacía
        with self.assertRaises(EmptyPosition):
            self.chess.validar(3, 3, 4, 4)  

    def test_validar_movimiento_invalido(self):
        # Intenta mover la torre a una posición no válida (
        with self.assertRaises(InvalidMove):
            self.chess.validar(0, 0, 1, 1)  

    
    