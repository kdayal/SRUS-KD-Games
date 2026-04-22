import unittest
from app.player import Player


class TestPlayer(unittest.TestCase):
    """
    Unit tests for the Player class properties and initialization.
    """

    def setUp(self):
        """Set up a standard player instance for testing."""
        self.test_id = "KD001"
        self.test_name = "Khushboo"
        self.player = Player(self.test_id, self.test_name)

    # ----------------------------
    # Existing tests 
    # ----------------------------
    def test_uid_property(self):
        self.assertEqual(self.player.uid, self.test_id)

    def test_name_property(self):
        self.assertEqual(self.player.name, self.test_name)

    def test_string_representation(self):
        expected_string = f"ID: {self.test_id} | Player: {self.test_name}"
        self.assertEqual(str(self.player), expected_string)

    # ----------------------------
    # NEW TEST (sorting - REQUIRED)
    # ----------------------------
    def test_sort_players(self):
        players = [
            Player("KD001", "Khushboo"),
            Player("KD002", "Alice"),
            Player("KD003", "Bob")
        ]

        # assign scores
        players[0].score = 10
        players[1].score = 5
        players[2].score = 15

        sorted_players = sorted(players)

        expected = [
            players[1],  # Alice (5)
            players[0],  # Khushboo (10)
            players[2]   # Bob (15)
        ]

        self.assertListEqual(sorted_players, expected)


if __name__ == '__main__':
    unittest.main()