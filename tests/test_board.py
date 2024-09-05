import unittest
from game.board import Board
from piezas.rook import Rook
from piezas.horse import Horse
from piezas.king import King


class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()

  
    def test_posiciones(self):

        # Verifica la posición de las torres negras
        self.assertIsInstance(self.board.get_piece(0,0), Rook) #BLACK
        self.assertIsInstance(self.board.get_piece(0,7), Rook) #BLACK
        
        # Verifica la posición de las torres blancas
        self.assertIsInstance(self.board.get_piece(7,0), Rook) #WHITE
        self.assertIsInstance(self.board.get_piece(7,7), Rook) #WHITE

        # Verifica la posición de los caballos negros
        self.assertIsInstance(self.board.get_piece(0,1), Horse)#BLACK
        self.assertIsInstance(self.board.get_piece(0,6), Horse) #BLACK
   

        # Verifica la posición de los caballos blancos
        self.assertIsInstance(self.board.get_piece(7,1), Horse)#WHITE
        self.assertIsInstance(self.board.get_piece(7,6), Horse) #WHITE

        #Verifica la posicion del rey blanco y negro
        self.assertIsInstance(self.board.get_piece(0,4), King)#WHITE
        self.assertIsInstance(self.board.get_piece(7,4), King) #BLACK

    

if __name__ == '__main__':
    unittest.main()