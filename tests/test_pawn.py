import unittest
from piezas.pawn import Pawn
from game.board import Board
from piezas.piece import Piece



class TestPawn(unittest.TestCase):

    def setUp(self):
        self.__board__ = Board()
        self.__pb__ = Pawn("BLACK")
        self.__pw__= Pawn("WHITE")
        self.board = Board(for_test=True)

    def test_primer_movimiento_peon(self):  #PEONES NEGROS CON DOBLE SALTO
        self.board.set_piece(6, 3, self.__pb__)
        movimientos = [(5, 3), (4, 3)]
        resultados = self.__pb__.movimiento_hacia_adelante(6, 3, es_primer_movimiento=True, board=self.board )
        self.assertEqual(resultados, movimientos)

    def test_no_primer_movimiento_peon(self):  # PEONES NEGROS
        self.board.set_piece(4, 3, self.__pb__)
        movimientos = [(3, 3)]
        resultados = self.__pb__.movimiento_hacia_adelante(4, 3, es_primer_movimiento=False, board=self.board )
        self.assertEqual(resultados, movimientos)

    def test_primer_movimiento_peon(self):  # PEONES BLANCO CON DOBLE SALTO
        self.board.set_piece(1, 3, self.__pw__)
        movimientos = [(2, 3), (3, 3)]
        resultados = self.__pw__.movimiento_hacia_adelante(1, 3, es_primer_movimiento=True, board=self.board )
        self.assertEqual(resultados, movimientos)

    def test_movimientos_con_compañeros_en_el_camino(self): #PEONES BLANCOS
        self.board.set_piece(3,3,self.__pw__)
        self.board.set_piece(4,3 , Piece("WHITE"))  
        movimientos= []
        resultados = self.__pw__.movimiento_hacia_adelante(3, 3, es_primer_movimiento=False, board=self.board )
        self.assertEqual(resultados, movimientos)
    def test_movimientos_con_compañeros_en_el_camino(self): #PEONES NEGROS
        self.board.set_piece(5,3,self.__pb__)
        self.board.set_piece(4,3 , Piece("BLACK"))  
        movimientos= []
        resultados = self.__pb__.movimiento_hacia_adelante(5, 3, es_primer_movimiento=False, board=self.board )
        self.assertEqual(resultados, movimientos)
    
    def test_movimientos_con_captura(self): #PEONES NEGROS
        self.board.set_piece(5,3,self.__pb__)
        self.board.set_piece(4,2 , Piece("WHITE"))  
        self.board.set_piece(4,4 , Piece("WHITE"))  
        movimientos = [(4,2),(4,4),(4,3)]
        resultados = self.__pb__.movimiento_hacia_adelante(5, 3, es_primer_movimiento=False, board=self.board )
        self.assertEqual(sorted(resultados), sorted(movimientos))
    
    def test_movimientos_con_captura_doble_salto(self): #PEONES BLANCOS
        self.board.set_piece(1,3,self.__pw__)
        self.board.set_piece(2,2 , Piece("BLACK"))  
        self.board.set_piece(2,4 , Piece("BLACK"))  
        movimientos = [(2,2),(2,4),(2,3),(3,3)]
        resultados = self.__pw__.movimiento_hacia_adelante(1, 3, es_primer_movimiento=True, board=self.board )
        self.assertEqual(sorted(resultados), sorted(movimientos))
    
    
       
       

      


if __name__ == '__main__':
    unittest.main()

   
