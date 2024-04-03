import unittest
from unittest.mock import patch
from game import Game
from player import Player
import random  # Assuming you import random for card selection


class TestGame(unittest.TestCase):

    def setUp(self):
        self.mock_player = Player("Benji")
        self.game = Game(self.mock_player)

    # @patch('game.__user_input', return_value=('TACO', 2))
    # @patch('game.random.choice', return_value='TACO')
    @patch.object(Game, '__user_input', return_value=('TACO', 2))
    def test_run_game_over(self, mock_private_method):
        self.assertFalse(self.game.run())
    #
    # @patch('builtins.input', side_effect=['TACO', 2])
    # @patch('game.random.choice', return_value='BOMB')
    # def test_run_game_over_with_bomb(self, mock_choice, mock_input):
    #     self.assertFalse(self.game.run())
    #
    # @patch('builtins.input', side_effect=['TACO', 2])
    # @patch('game.random.choice', return_value='PIZZA')
    # def test_run_game_success(self, mock_choice, mock_input):
    #     self.assertTrue(self.game.run())
    #     self.assertEqual(self.mock_player.score, 1)
    #

if __name__ == '__main__':
    unittest.main()
