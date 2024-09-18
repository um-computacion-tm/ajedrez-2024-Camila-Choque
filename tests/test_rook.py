
import unittest
from piezas.rook import Rook
from game.board import Board
from piezas.piece import Piece


class TestRook(unittest.TestCase):

    def setUp(self):
        self.__board__ = Board()
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.__rb__ = Rook("black")
        self.__rw__= Rook("white")
       

   
    def test_movimientos_verticales_con_compañeros_en_el_camino(self): #BLANCAS
        self.board[4][1] = self.__rw__
        self.board[2][1] = Piece("white")  
        self.board[6][1] = Piece("white")
        resultados= [(3, 1), (5, 1)]
        self.assertEqual(self.__rw__.posiciones_verticales(4, 1, self.board), resultados)

    def test_movimientos_verticales_con_compañeros_en_el_camino(self): #NEGRAS
        self.board[4][3] = self.__rb__
        self.board[2][3] = Piece("black")  
        self.board[6][3] = Piece("black")
        resultados= [(3, 3), (5, 3)]
        self.assertEqual(self.__rb__.posiciones_verticales(4, 3, self.board), resultados)

    

        


if __name__ == '__main__':
    unittest.main()

