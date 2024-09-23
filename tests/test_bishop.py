import unittest
from piezas.bishop import Bishop
from game.board import Board
from piezas.piece import Piece




class TestPawn(unittest.TestCase):

    def setUp(self):
        self.__board__ = Board()
        self.__bb__ = Bishop("BLACK")
        self.__bw__= Bishop("WHITE")
        self.board = Board(for_test=True)

    def test_movimientos(self):  #ALFIL BLANCO
        self.board.set_piece(4,3 ,self.__bw__)
        movimientos = [(5, 4), (6, 5), (7, 6),(5, 2), (6, 1), (7, 0),(3, 4), (2, 5), (1, 6), (0, 7),(3, 2), (2, 1), (1, 0)]
        self.assertEqual(self.__bw__.movimiento(4, 3, self.board), movimientos)

    def test_movimientos(self):  #ALFIL NEGRO
        self.board.set_piece(0,2 ,self.__bb__)
        movimientos = [(1, 3), (2, 4), (3, 5), (4, 6), (5, 7),(1, 1), (2, 0)]
        self.assertEqual(self.__bb__.movimiento(0, 2, self.board), movimientos)

    def test_movimientos_con_compañeros_en_el_camino(self): #ALFILES NEGROS
        self.board.set_piece(5,3,self.__bb__)
        self.board.set_piece(4,2 , Piece("BLACK"))  
        self.board.set_piece(4,4 , Piece("BLACK"))
        resultados= [(6,2),(7,1),(6,4),(7,5)] 
        resultado_esperado = self.__bb__.movimiento(5, 3, self.board)
        self.assertEqual(sorted(resultado_esperado), sorted(resultados))
    def test_movimientos_con_captura(self): #ALFILES NEGROS
        self.board.set_piece(5,3,self.__bb__)
        self.board.set_piece(4,2 , Piece("WHITE"))  
        self.board.set_piece(4,4 , Piece("WHITE"))
        resultados= [(4,2),(4,4),(6,2),(7,1),(6,4),(7,5)] 
        resultado_esperado = self.__bb__.movimiento(5, 3, self.board)
        self.assertEqual(sorted(resultado_esperado), sorted(resultados))
    
    if __name__ == '__main__':
      unittest.main()

   
    