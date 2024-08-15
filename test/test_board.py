import unittest
from game.board import Board
from piece.rook import Rook

class TestBoard(unittest.TestCase):

    def test_init(self):
        board = Board()
        self.assertEqual(len(board.grid),8,)
        self.assertEqual(len(board.grid[0]),8,)

        # Verifica la posición de las torres negras
        self.assertIsInstance(board._Board__positions__[0][0], Rook)
        self.assertEqual(board._Board__positions__[0][0].color, "BLACK")
        self.assertIsInstance(board._Board__positions__[0][7], Rook)
        self.assertEqual(board._Board__positions__[0][7].color, "BLACK")

        # Verifica la posición de las torres blancas
        self.assertIsInstance(board._Board__positions__[7][0], Rook)
        self.assertEqual(board._Board__positions__[7][0].color, "WHITE")
        self.assertIsInstance(board._Board__positions__[7][7], Rook)
        self.assertEqual(board._Board__positions__[7][7].color, "WHITE")

if __name__ == '__main__':
    unittest.main()