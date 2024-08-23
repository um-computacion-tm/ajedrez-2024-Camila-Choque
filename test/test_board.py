import unittest
from game.board import Board
from piezas.rook import Rook
from piezas.queen import Queen
from piezas.horse import Horse

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()

""""      
    def test_posiciones(self):

        # Verifica la posición de las torres negras
        self.assertIsInstance(Board.get_piece[0][0], Rook) #BLACK
        self.assertIsInstance(board.get_piece[0][7], Rook) #BLACK
        
        # Verifica la posición de las torres blancas
        self.assertIsInstance(board.get_piece[7][0], Rook) #WHITE
        self.assertIsInstance(board.get_piece[7][7], Rook) #WHITE

        # Verifica la posición de la reina negra
        self.assertIsInstance(board.get_piece[0][3], Queen) #BLACK
      
        # Verifica la posición de la reina blancas
        self.assertIsInstance(board.get_piece[7][3], Queen)#WHITE
        

        # Verifica la posición de los caballos negros
        self.assertIsInstance(board.get_piece[0][2], Horse)#BLACK
        self.assertIsInstance(board.get_piece[0][5], Horse) #BLACK
   

        # Verifica la posición de los caballos blancos
        self.assertIsInstance(board.get_piece[7][2], Horse)#WHITE
        self.assertIsInstance(board.get_piece[7][5], Horse) #WHITE
   
"""


if __name__ == '__main__':
    unittest.main()