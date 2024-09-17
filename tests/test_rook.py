
import unittest
from piezas.rook import Rook
from game.board import Board
from piezas.piece import Piece


class TestRook(unittest.TestCase):

    def setUp(self):
        self.__board__ = Board()
        self.__rook__ = Rook("WHITE")
        self.__rook__=Rook("BLACK")
       

   
    def test_move_vertical_desc_sin_otras_piezas(self): #sin otras piezas del mismo color en el camino
        board = Board()
        rook = Rook(color='white')
        board.set_piece(2, 4, rook)  
        # Supongamos que no hay otras piezas en el camino
        movimientos = rook.possible_positions_vd(2, 4, board)
        resultados = [(3, 4), (4, 4), (5, 4), (6, 4)]
        self.assertEqual(resultados, movimientos)
    def test_move_vertical_desc_mismo_color(self):
        board = Board()
        rook = Rook(color='white')
        board.set_piece(2, 4, rook)
        # Colocar otra pieza del mismo color en el camino
        same_color_piece = Piece(color='white')
        board.set_piece(5, 4, same_color_piece)
        # Calcular los movimientos posibles hacia abajo
        movimientos = rook.possible_positions_vd(2, 4, board)
        resultados = [(3, 4), (4, 4)]
        self.assertEqual(resultados, movimientos)

   
        
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

