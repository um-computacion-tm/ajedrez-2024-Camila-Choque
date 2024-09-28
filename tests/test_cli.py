import unittest

from unittest.mock import patch
from game.chess import Chess
from cli import play

class TestCli(unittest.TestCase):

    @patch(  # este patch controla lo que hace el input
        'builtins.input',
        side_effect=['1', '1', '2', '2'], # estos son los valores que simula lo que ingresaria el usuario
    )

    @patch('builtins.print') # este patch controla lo que hace el print
    @patch.object(Chess, 'validar')

    def test_happy_path(self,mock_chess_validar,mock_print,mock_input,): #

        chess = Chess()
        play(chess)
        self.assertEqual(mock_input.call_count, 5)
        self.assertEqual(mock_print.call_count, 12)
        self.assertEqual(mock_chess_validar.call_count, 0)

    @patch(  # este patch controla lo que hace el input
        'builtins.input',
        side_effect=['hola', '1', '2', '2'], # estos son los valores que simula lo que ingresaria el usuario
    )

    @patch('builtins.print') # este patch controla lo que hace el print
    @patch.object(Chess, 'validar')

    def test_not_happy_path(self,mock_chess_validar,mock_print,mock_input,):

        chess = Chess()
        play(chess)
        self.assertEqual(mock_input.call_count, 1)
        self.assertEqual(mock_print.call_count, 12)
        self.assertEqual(mock_chess_validar.call_count, 0)

    @patch(  # este patch controla lo que hace el input
        'builtins.input',
        side_effect=['1', '1', '2', 'hola'], # estos son los valores que simula lo que ingresaria el usuario
    )

    @patch('builtins.print') # este patch controla lo que hace el print
    @patch.object(Chess, 'validar')

    def test_more_not_happy_path(self,mock_chess_validar,mock_print,mock_input,): #

        chess = Chess()
        play(chess)
        self.assertEqual(mock_input.call_count, 4)
        self.assertEqual(mock_print.call_count, 12)
        self.assertEqual(mock_chess_validar.call_count, 0)

   