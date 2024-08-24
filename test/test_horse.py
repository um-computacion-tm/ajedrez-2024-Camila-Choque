import unittest
from piezas.horse import Horse


class TestHorse(unittest.TestCase):
    def setUp(self):
        
        self.horse = Horse("BLACK")

    def test_horse_moves_44(self):  #LA PISCION ES (4,4)
        resultado_posicion_central = [(6,5),(6,3),(2,5),(2,3),(5,6),(5,2),(3,6),(3,2)]
        resultado = self.horse.horse_moves(4, 4)
        self.assertEqual(resultado,resultado_posicion_central)

    

        

if __name__ == '__main__':
    unittest.main()