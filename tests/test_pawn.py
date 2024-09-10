import unittest
from piezas.pawn import Pawn
from game.board import Board
from piezas.piece import Piece


class MockBoard:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]

    def get_piece(self, row, col):
        return self.board[row][col]

    def set_piece(self, row, col, piece):
        self.board[row][col] = piece

class MockPiece:
    def __init__(self, color):
        self.color = color

class TestPawn(unittest.TestCase):

    def setUp(self):
        self.__board__ = Board()
        self.__pawn__ = Pawn("WHITE")
      

    def test_movimientos_basicos_hacia_adelante(self):  # Peón blanco
        movimientos = [(2, 1), (3, 1)]  # El peón blanco puede avanzar una o dos casillas en su primer movimiento
        resultados = self.__pawn__.movimiento_hacia_adelante(1, 1, es_primer_movimiento=True, color="white",board=self.__board__)
        self.assertEqual(resultados, movimientos)

    def test_movimientos_basicos_hacia_adelante(self):  # Peón negro
        movimientos = [(5, 0), (4, 0)]  # El peón blanco puede avanzar una o dos casillas en su primer movimiento
        resultados = self.__pawn__.movimiento_hacia_adelante(6, 0, es_primer_movimiento=True, color="black",board=self.__board__)
        self.assertEqual(resultados, movimientos)

    def test_movimientos_basicos_hacia_adelante_no_primer_movimiento(self):  # Peón negro
        movimientos = [(2, 0)]  # El peón negro solo avanza una casilla después de su primer movimiento
        resultados = self.__pawn__.movimiento_hacia_adelante(3, 0, es_primer_movimiento=False, color="black",board=self.__board__)
        self.assertEqual(resultados, movimientos)

    def test_movimientos_basicos_hacia_adelante_no_primer_movimiento(self):  # Peón blanco
        movimientos = [(4, 0)]  # El peón blanco solo avanza una casilla después de su primer movimiento
        resultados = self.__pawn__.movimiento_hacia_adelante(3, 0, es_primer_movimiento=False, color="white",board=self.__board__)
        self.assertEqual(resultados, movimientos) 

    
    def test_pawn_captures_diagonally(self):
        # Crear el tablero vacío
        board = MockBoard()
        # Añadir una pieza enemiga en diagonal para que el peón pueda capturarla
        enemy_piece = MockPiece('black')  #La pieza enemiga es negra
        board.set_piece(3, 2, enemy_piece)  #Colocar la pieza en (3, 2)
        # Crear el peón blanco en la posición (2, 1)
        pawn = Pawn("white") 
        posibles = pawn.movimiento_hacia_adelante(2, 1, False, 'white', board)
        # Verificar que el peón puede capturar la pieza en (3, 2)
        self.assertIn((3, 2), posibles)




if __name__ == '__main__':
    unittest.main()

   
