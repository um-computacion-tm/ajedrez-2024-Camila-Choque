import unittest
from piezas.horse import Horse
from game.board import Board



class TestHorse(unittest.TestCase):
    def setUp(self):
        
        self.__hw__ = Horse("WHITE")  
        self.__hb__ = Horse("BLACK")  
        self.board = Board(for_test=True) 

    def test_movimientos_caballo(self):  #CABALLOS BALNCOS
        self.board.set_piece(4,3 ,self.__hw__)
        movimientos = [(6, 4),(6, 2),(2, 4),(2, 2),(5, 5), (5, 1),(3, 5),(3, 1)]
        resultados = self.__hw__.horse_moves(4, 3, self.board)
        self.assertEqual(resultados, movimientos)

     


"""""
    def test_horse_moves_44(self):  #LA PISCION ES (4,4)
        resultado_posicion_central = [(6,5),(6,3),(2,5),(2,3),(5,6),(5,2),(3,6),(3,2)]
        resultado = self.horse.horse_moves(4, 4)
        self.assertEqual(resultado,resultado_posicion_central)

    def test_horse_moves_00(self):  #LA PISCION ESQUINA ES(0,0)
        resultado_posicion_esquina = [(2,1),(1,2)]
        resultado = self.horse.horse_moves(0,0)
        self.assertEqual(resultado,resultado_posicion_esquina)

    def test_horse_moves_07(self):  #LA PISCION BORDE ES (0,7)
        resultado_posicion_borde = [(2,6),(1,5)]
        resultado = self.horse.horse_moves(0,7)
        self.assertEqual(resultado,resultado_posicion_borde)

    def test_horse_moves_74(self):  #LA PISCION DE UN BORDE PERO NO EN UNA ESQUINA, ES (7,4)
        resultado_posicion = [(5,5),(5,3),(6,6),(6,2)]
        resultado = self.horse.horse_moves(7,4)
        self.assertEqual(resultado,resultado_posicion)
        
   ##ESTA AHI FUNCIONA 
"""""

    

        

if __name__ == '__main__':
    unittest.main()