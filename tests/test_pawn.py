import unittest
from piezas.pawn import Pawn
from game.board import Board

class TestPawn(unittest.TestCase):

    def setUp(self):
        self.__board__ = Board()
        self.__pawn__ = Pawn("WHITE")
      

    def test_movimientos_basicos_hacia_adelante(self):  # Peón blanco
        movimientos = [(2, 1), (3, 1)]  # El peón blanco puede avanzar una o dos casillas en su primer movimiento
        resultados = self.__pawn__.movimiento_hacia_adelante(1, 1, es_primer_movimiento=True, color="white")
        self.assertEqual(resultados, movimientos)

    def test_movimientos_basicos_hacia_adelante(self):  # Peón negro
        movimientos = [(5, 0), (4, 0)]  # El peón blanco puede avanzar una o dos casillas en su primer movimiento
        resultados = self.__pawn__.movimiento_hacia_adelante(6, 0, es_primer_movimiento=True, color="black")
        self.assertEqual(resultados, movimientos)

    def test_movimientos_basicos_hacia_adelante_no_primer_movimiento(self):  # Peón negro
        movimientos = [(2, 0)]  # El peón negro solo avanza una casilla después de su primer movimiento
        resultados = self.__pawn__.movimiento_hacia_adelante(3, 0, es_primer_movimiento=False, color="black")
        self.assertEqual(resultados, movimientos)

    def test_movimientos_basicos_hacia_adelante_no_primer_movimiento(self):  # Peón blanco
        movimientos = [(4, 0)]  # El peón blanco solo avanza una casilla después de su primer movimiento
        resultados = self.__pawn__.movimiento_hacia_adelante(3, 0, es_primer_movimiento=False, color="white")
        self.assertEqual(resultados, movimientos)

    

   

    #ARREGLAR