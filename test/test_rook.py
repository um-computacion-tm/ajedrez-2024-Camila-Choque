import unittest
from piezas.rook import Rook

class TestRook(unittest.TestCase):
    def setUp(self):
        self.rook = Rook
    def test_rook(self):
        coordenada1 = 1
        coordenada2 = 0
        resultado = self.rook.valid_move_rook(coordenada1, coordenada2)
        self.assertEqual(resultado,True)

    
   

if __name__ == '__main__':
    unittest.main()