import unittest
from player import Player  # assuming your class is in a file named player.py


class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player("Benji")

    def test_increment_score(self):
        self.player.increment_score()
        self.assertEqual(self.player.get_score(), 1)

    def test_get_name(self):
        self.assertEqual(self.player.get_name(), "Benji")

    def test_get_score(self):
        self.assertEqual(self.player.get_score(), 0)


if __name__ == '__main__':
    unittest.main()
