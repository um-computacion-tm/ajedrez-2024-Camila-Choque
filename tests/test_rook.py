
import unittest
from piezas.rook import Rook
from game.board import Board
from piezas.pawn import Pawn


class TestRook(unittest.TestCase):

    def setUp(self):
        self.__board__ = Board()
        self.__rook__ = Rook("WHITE")
        self.__rook__=Rook("BLACK")
        self.__board__.set_piece(0, 0, self.__rook__)

   
    def test_move_vertical_desc(self):
        movimientos = [(3,4),(4,4),(5,4),(6,4),(7,4)]
        resultados = self.__rook__.possible_positions_vd(2,4,)
        self.assertEqual(resultados,movimientos)
        
"""""
    def test_move_vertical_asc(self):
        movimientos = [(4,4),(3,4),(2,4),(1,4),(0,4)]
        resultados = self.__rook__.possible_positions_va(5,4)
        self.assertEqual(resultados,movimientos)

    def test_move_horzontal_derecha(self):
        movimientos = [(2,4),(2,5),(2,6),(2,7)]
        resultados = self.__rook__.possible_positions_derecha(2,3)
        self.assertEqual(resultados,movimientos)

    def test_move_horizontal_izquierda(self):
        movimientos = [(2,2),(2,1),(2,0)]
        resultados = self.__rook__.possible_positions_izquierda(2,3)
        self.assertEqual(resultados,movimientos)

"""""


if __name__ == '__main__':
    unittest.main()

