
import unittest
from piezas.rook import Rook
from game.board import Board


class TestRook(unittest.TestCase):

    def setUp(self):
        self.__board__ = Board()
        self.__rook__ = Rook("WHITE")
        self.__board__.set_piece(0, 0, self.__rook__)

   
    def test_move_vertical_desc(self):
        movimientos = [(3,4),(4,4),(5,4),(6,4),(7,4)]
        resultados = self.__rook__.possible_position_vd(2,4)
        self.assertEqual(resultados,movimientos)

   
  
  


if __name__ == '__main__':
    unittest.main()

