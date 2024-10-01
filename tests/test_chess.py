import unittest
from game.chess import Chess
from game.board import Board
from game.exceptions import InvalidMove
from game.exceptions import InvalidTurn
from game.exceptions import EmptyPosition
from piezas.rook import Rook
from piezas.king import King

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

     self.assertEqual(self.chess.turn, "WHITE")
     self.chess.change_turn()
     self.assertEqual(self.chess.turn, "BLACK")
     self.chess.change_turn()
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

    def test_turno_invalido(self):
    
        board = Board(for_test=True)
        board.set_piece(0, 0, Rook("BLACK"))
        setattr(self.chess, '_Chess__board__', board)
        with self.assertRaises(InvalidTurn):
            self.chess.validar(0, 0, 1, 0)

    def test_movimiento_invalido(self):
      
        board = Board(for_test=True)
        board.set_piece(7, 0, Rook("WHITE"))
        setattr(self.chess, '_Chess__board__', board)
        with self.assertRaises(InvalidMove):
            self.chess.validar(7, 0, 6, 1)

    def test_reyes_presentes(self):
        self.chess.__board__.set_piece(7, 4, King("WHITE"))
        self.chess.__board__.set_piece(0, 4, King("BLACK"))
        self.chess.check_kings()
        self.assertTrue(self.chess.is_playing())
        self.assertIsNone(self.chess.check_kings())

    def test_validar_fin_del_juego(self):
         self.chess.__board__.set_piece(0, 4, King("BLACK"))
         self.chess.__board__.set_piece(1, 4, Rook("WHITE"))
         self.chess.validar(1, 4, 0, 4)
         self.assertFalse(self.chess.is_playing)
         result = self.chess.check_kings()
         self.assertEqual(result, "WHITE")




if __name__ == '__main__':
    unittest.main()
    
    