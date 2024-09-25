import unittest
from piezas.king import King
from game.board import Board
from piezas.piece import Piece
class TestHorse(unittest.TestCase):

    def setUp(self):
        self.__board__ = Board()
        self.__kb__ = King("BLACK")
        self.__kw__= King("WHITE")
        self.board = Board(for_test=True)
    def test_movimientos(self):  #REY BLANCO
        self.board.set_piece(7,4 ,self.__kw__)
        movimientos = [(6,3),(6,4),(6,5),(7,3),(7,5)]
        resultado = self.__kw__.movimientos_rey(7, 4, self.board)
        self.assertEqual(sorted(resultado),sorted(movimientos))

    def test_captura(self):  #REY BLANCO
        self.board.set_piece(7,4 ,self.__kw__)
        self.board.set_piece(6,3 , Piece("BLACK"))  
        self.board.set_piece(6,4 , Piece("BLACK"))  
        self.board.set_piece(6,5 , Piece("BLACK"))  
        self.board.set_piece(7,3, Piece("BLACK"))  
        self.board.set_piece(7,5 , Piece("BLACK"))  
        movimientos = [(6,3),(6,4),(6,5),(7,3),(7,5)]
        resultado = self.__kw__.movimientos_rey(7, 4, self.board)
        self.assertEqual(sorted(resultado),sorted(movimientos))

    def test_movimientos_con_compañeros(self):  #REY BLANCO
        self.board.set_piece(7,2 ,self.__kw__)
        self.board.set_piece(6,1 , Piece("WHITE"))  
        self.board.set_piece(6,2 , Piece("WHITE"))
        self.board.set_piece(6,3 , Piece("WHITE"))  
        self.board.set_piece(7,3 , Piece("WHITE"))  
        movimientos = [(7,1)]
        resultado = self.__kw__.movimientos_rey(7, 2, self.board)
        self.assertEqual(sorted(resultado),sorted(movimientos))

    

    

if __name__ == '__main__':
    unittest.main()

        