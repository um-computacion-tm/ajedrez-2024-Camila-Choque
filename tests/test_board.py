import unittest
from game.board import Board
from piezas.rook import Rook
from piezas.horse import Horse
from piezas.king import King
from piezas.bishop import Bishop
from piezas.queen import Queen
from piezas.pawn import Pawn
from game.exceptions import OutOfBoard


class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()

    
    """
    def test_str_board(self):
        board = Board()
        self.assertEqual(
            str(board),
            (
                "♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖ \n"
                "♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙ \n"
                "                \n"
                "                \n"
                "                \n"
                "                \n"
                "♟ ♟ ♟ ♟ ♟ ♟ ♟ ♟ \n"
                "♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜ \n"
            )
        )


    def test_move(self):
        board = Board(for_test=True)
        rook = Rook(color='black')
        board.set_piece(0, 0, rook)

        board.move(
            from_row=0,
            from_col=0,
            to_row=0,
            to_col=1,
        )

        self.assertIsInstance(
            board.get_piece(0, 1),
            Rook,
        )
        self.assertEqual(
            str(board),
            (
                " ♖      \n"
                "        \n"
                "        \n"
                "        \n"
                "        \n"
                "        \n"
                "        \n"
                "        \n"
            )
        )
     """
    def test_get_piece_out_of_range(self):
        board = Board(for_test=True)

        with self.assertRaises(OutOfBoard) as exc:
            board.get_piece(10, 10)

        self.assertEqual(
            exc.exception.message,
            "La posicion indicada se encuentra fuera del tablero"
        )
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

        #Verifica la posicion de los alfiles blanco y negro
        self.assertIsInstance(self.board.get_piece(0, 2), Bishop)
        self.assertIsInstance(self.board.get_piece(0, 5), Bishop)
        self.assertIsInstance(self.board.get_piece(7, 2), Bishop)
        self.assertIsInstance(self.board.get_piece(7, 5), Bishop)

        #Verifica la posicion de las reinas  blanco y negro
        self.assertIsInstance(self.board.get_piece(0, 3), Queen)
        self.assertIsInstance(self.board.get_piece(7, 3), Queen)

       
        for i in range(8):
            self.assertIsInstance(self.board.get_piece(1, i), Pawn)
            self.assertIsInstance(self.board.get_piece(6, i), Pawn)


    def test_ver_movimientos_validos(self):
        board = Board(for_test=True)
        rook = Rook(color='BLACK')
        board.set_piece(3, 3, rook)

        movimientos = board.ver_movimientos_validos(3, 3)
        esperado = []
        for i in range(8):
            if i != 3:
                esperado.append((3, i))
                esperado.append((i, 3))

        # Verificar que los movimientos válidos sean los esperados
        self.assertEqual(sorted(movimientos), sorted(esperado))
        self.assertEqual(sorted(movimientos), sorted(esperado))


    

if __name__ == '__main__':
    unittest.main()