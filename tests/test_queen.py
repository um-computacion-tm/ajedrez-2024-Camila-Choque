
import unittest
from game.board import Board
from piezas.queen import Queen
from piezas.piece import Piece
class TestPawn(unittest.TestCase):

    def setUp(self):
        self.__board__ = Board()
        self.__qb__ = Queen("BLACK")
        self.__qw__= Queen("WHITE")
        self.board = Board(for_test=True)

    def test_movimientos(self):  #REINA BLANCA
        self.board.set_piece(4,3 ,self.__qw__)
        movimientos = [(3,3), (2,3), (1,3), (0,3), (5,3), (6,3), (7,3),(4,2), (4,1), (4,0), (4,4), (4,5), (4,6), (4,7),(3,4), (2,5), (1,6), (0,7), (3,2), (2,1), (1,0), (5,4), (6,5), (7,6), (5,2), (6,1), (7,0)]
        resultado = self.__qw__.movimiento(4, 3, self.board)
        self.assertEqual(sorted(resultado),sorted(movimientos))

    def test_movimientos_con_compañeros(self):  #REINA BLANCA
        self.board.set_piece(4,3 ,self.__qw__)
        self.board.set_piece(4,2 , Piece("WHITE"))  
        self.board.set_piece(4,4 , Piece("WHITE"))
        self.board.set_piece(3,2 , Piece("WHITE"))  
        self.board.set_piece(5,2 , Piece("WHITE"))
        self.board.set_piece(3,3 , Piece("WHITE"))  
        self.board.set_piece(5,3 , Piece("WHITE"))
        self.board.set_piece(3,4 , Piece("WHITE"))  
        self.board.set_piece(5,4 , Piece("WHITE"))
        movimientos = []
        resultado = self.__qw__.movimiento(4, 3, self.board)
        self.assertEqual(sorted(resultado),sorted(movimientos))

    def test_captura(self):  #REINA BLANCA
        self.board.set_piece(6,3 ,self.__qw__)
        self.board.set_piece(5,2 , Piece("BLACK"))  
        self.board.set_piece(5,3 , Piece("BLACK"))
        self.board.set_piece(5,4 , Piece("BLACK"))
        movimientos = [(5,2),(5,3),(5,4),(6,0),(6,1),(6,2),(6,4),(6,5),(6,6),(6,7),(7,3),(7,2),(7,4)]
        resultado = self.__qw__.movimiento(6, 3, self.board)
        self.assertEqual(sorted(resultado),sorted(movimientos))
if __name__ == '__main__':
    unittest.main()
    