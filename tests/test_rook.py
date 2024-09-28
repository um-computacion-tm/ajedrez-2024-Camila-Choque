
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
        self.board = Board(for_test=True)

   

    def test_movimientos_con_compañeros_en_el_camino(self): #NEGRAS
        self.board.set_piece(4,3 ,self.__rb__)
        self.board.set_piece(2,3 , Piece("black"))  
        self.board.set_piece(6,3 , Piece("black"))
        resultados= [(3, 3), (5, 3),(4,0),(4,1),(4,2),(4,4),(4,5),(4,6),(4,7)]
        esperado = self.__rb__.movimiento(4, 3, self.board)
        self.assertEqual(sorted(esperado),sorted(resultados))

    def test_movimientos_con_compañeros_en_el_camino(self): #BLANCAS
        self.board.set_piece(4,3,self.__rw__)
        self.board.set_piece(4,1 , Piece("white"))  
        self.board.set_piece(4,5 , Piece("white"))
        resultados= [(4, 2), (4, 4),(0,3),(1,3),(2,3),(3,3),(5,3),(6,3),(7,3)]
        esperado = self.__rw__.movimiento(4, 3, self.board)
        self.assertEqual(sorted(esperado), sorted(resultados))

    def test_movimientos(self):  #BLANCAS
        self.board.set_piece(4,3 ,self.__rw__)
        movimientos = [(4,0),(4,1),(4,2),(4,4),(4,5),(4,6),(4,7),(0,3),(1,3),(2,3),(3,3),(5,3),(6,3),(7,3)]
        self.assertEqual(self.__rw__.movimiento(4, 3, self.board), movimientos)

    def test_movimientos(self):  #BLANCAS
        self.board.set_piece(4,3 ,self.__rw__)
        movimientos = [(0,3),(1,3),(2,3),(3,3),(5,3),(6,3),(7,3),(4,0),(4,1),(4,2),(4,4),(4,5),(4,6),(4,7)]
        esperado = self.__rw__.movimiento(4, 3, self.board)
        self.assertEqual(sorted(esperado), sorted(movimientos))

    def test_movimientos_con_captura(self): #BLANCAS
        self.board.set_piece(2,3,self.__rw__)
        self.board.set_piece(2,1 , Piece("black"))  
        self.board.set_piece(2,5 , Piece("black"))
        resultados= [(2,2),(2,1),(2,4),(2,5),(0,3),(1,3),(2,3),(3,3),(5,3),(6,3),(7,3)]
        resultados_obtenidos = sorted(self.__rw__.movimiento(2, 3, self.board))
        self.assertEqual(sorted(resultados_obtenidos), sorted(resultados))

    def test_movimientos_con_captura(self): #BLANCAS
        self.board.set_piece(2,3,self.__rw__)
        self.board.set_piece(0,3 , Piece("black"))  
        self.board.set_piece(4,3 , Piece("black"))
        resultados= [(2,0),(2,1),(2,2),(2,4),(2,5),(2,6),(2,7),(3,3),(4,3),(1,3),(0,3)]
        resultados_obtenidos = sorted(self.__rw__.movimiento(2, 3, self.board))
        self.assertEqual(sorted(resultados_obtenidos), sorted(resultados))

    def test_movimientos_con_captura_y_compañero(self): #BLANCAS
        self.board.set_piece(2,3,self.__rw__)
        self.board.set_piece(0,3 , Piece("black"))  
        self.board.set_piece(1,3 , Piece("white"))
        self.board.set_piece(3,3 , Piece("black"))
        resultados= [(3,3),(2,0),(2,1),(2,2),(2,4),(2,5),(2,6),(2,7)]
        resultados_obtenidos = sorted(self.__rw__.movimiento(2, 3, self.board))
        self.assertEqual(sorted(resultados_obtenidos), sorted(resultados))

    def test_movimientos_horizontal_con_captura_y_compañero(self): #BLANCAS
        self.board.set_piece(2,3,self.__rw__)
        self.board.set_piece(2,1 , Piece("black"))  
        self.board.set_piece(2,2 , Piece("white"))
        self.board.set_piece(2,4 , Piece("black"))
        resultados= [(2,4),(0,3),(1,3),(3,3),(4,3),(5,3),(6,3),(7,3)]
        resultados_obtenidos = sorted(self.__rw__.movimiento(2, 3, self.board))
        self.assertEqual(sorted(resultados_obtenidos), sorted(resultados))
    
    
        
    
        
    
    

if __name__ == '__main__':
    unittest.main()

