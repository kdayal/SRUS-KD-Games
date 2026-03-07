import unittest
from app.player import Player

class TestPlayer(unittest.TestCase):
    """
    Unit tests for the Player class properties and initialization.
    """

    def setUp(self):
        """Set up a standard player instance for testing with personalized data."""
        self.test_id = "KD001" 
        self.test_name = "Khushboo"
        self.player = Player(self.test_id, self.test_name)

    def test_uid_property(self):
        """Verify that the UID property returns the correct value."""
        self.assertEqual(self.player.uid, self.test_id)

    def test_name_property(self):
        """Verify that the Name property returns the correct value."""
        self.assertEqual(self.player.name, self.test_name)

    def test_string_representation(self):
       
        expected_string = f"ID: {self.test_id} | Player: {self.test_name}"
        self.assertEqual(str(self.player), expected_string)

if __name__ == '__main__':
    unittest.main()