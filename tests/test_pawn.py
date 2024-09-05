import unittest
from piezas.pawn import Pawn
from game.board import Board

class TestPawn(unittest.TestCase):

    def setUp(self):
        self.__board__ = Board()
        self.__pawn__ = Pawn("WHITE")
        self.__board__.set_piece(6, 0, self.__pawn__)


    def test_movimientos_basicos_hacia_adelante(self):
        movimientos = [(2,1),(3,1),(4,1),(5,1),(6,1),(7,1)]
        resultados = self.__pawn__.movimiento_hacia_adelante(1,1)
        self.assertEqual(resultados,movimientos)

    #ARREGLAR