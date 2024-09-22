import unittest
from piezas.horse import Horse
from game.board import Board
from piezas.piece import Piece



class TestHorse(unittest.TestCase):
    def setUp(self):
        
        self.__hw__ = Horse("WHITE")  
        self.__hb__ = Horse("BLACK")  
        self.board = Board(for_test=True) 

    def test_movimientos_caballo(self):  #CABALLOS BLANCOS
        self.board.set_piece(4,3 ,self.__hw__)
        movimientos = [(6, 4),(6, 2),(2, 4),(2, 2),(5, 5), (5, 1),(3, 5),(3, 1)]
        resultados = self.__hw__.horse_moves(4, 3, self.board)
        self.assertEqual(resultados, movimientos)

    def test_movimientos_con_compañeros_en_el_camino(self): #CABALLOS BLANCOS
        self.board.set_piece(4,3,self.__hw__)
        self.board.set_piece(5,1 , Piece("WHITE"))  
        self.board.set_piece(5,5 , Piece("WHITE"))
        resultados= [(6, 4),(6, 2),(2, 4),(2, 2),(3, 5),(3, 1)]
        resultado_esperado = self.__hw__.horse_moves(4, 3, self.board)
        self.assertEqual(sorted(resultado_esperado), sorted(resultados))

    def test_movimientos_con_compañeros_en_el_camino(self): #CABALLOS NEGROS
        self.board.set_piece(2,4,self.__hb__)
        self.board.set_piece(4,5 , Piece("BLACK"))  
        self.board.set_piece(4,3 , Piece("BLACK"))
        resultados= [(3, 6),(3, 2),(1, 6),(1, 2),(0,5),(0,3)] #(0,5) y (0,3) estan fuera del tablero?
        resultado_esperado = self.__hb__.horse_moves(2, 4, self.board)
        self.assertEqual(sorted(resultado_esperado), sorted(resultados))

    def test_movimientos_con_captura(self): #BLANCAS
        self.board.set_piece(4,4,self.__hw__)
        self.board.set_piece(6,5 , Piece("BLACK"))  
        self.board.set_piece(6,3 , Piece("BLACK"))  
        resultados_obtenidos = self.__hw__.captura(6,5, self.board)
        resultados_obtenidos_2 = self.__hw__.captura(6,3, self.board)
        self.assertTrue(resultados_obtenidos)
        self.assertTrue(resultados_obtenidos_2)
        self.assertFalse(self.__hw__.captura(0,1, self.board)) #No existe

    
     


        

if __name__ == '__main__':
    unittest.main()