import unittest
from app.player import Player
from app.player_list import PlayerList

class TestPlayerList(unittest.TestCase):
    def setUp(self):
        """Set up an empty list and a player for testing."""
        self.list = PlayerList()
        self.p1 = Player("KD001", "Khushboo")

    def test_is_empty_initially(self):
        """Check if the list starts empty."""
        self.assertTrue(self.list.is_empty())

    def test_insert_head(self):
        """Verify inserting at the head."""
        self.list.insert_head(self.p1)
        self.assertFalse(self.list.is_empty())
        self.assertEqual(self.list._head.player.name, "Khushboo")

    def test_insert_tail(self):
        """Verify inserting at the tail."""
        p2 = Player("KD002", "Amit")
        self.list.insert_head(self.p1)
        self.list.insert_tail(p2)
        
        
        self.assertEqual(self.list._tail.player.name, "Amit")
       
        self.assertEqual(self.list._head.next.player.name, "Amit")

    def test_delete_head(self):
        """Verify deleting from the head."""
        self.list.insert_head(self.p1)
        self.list.delete_head()
        self.assertTrue(self.list.is_empty())

    def test_delete_by_key(self):
        """Verify deleting a specific player by their ID."""
        p2 = Player("KD002", "Amit")
        self.list.insert_head(self.p1)
        self.list.insert_tail(p2)
        
        # Delete Amit by ID
        result = self.list.delete_by_key("KD002")
        self.assertTrue(result)
        # Check if Khushboo is now both head and tail
        self.assertEqual(self.list._head.player.name, "Khushboo")
        self.assertIsNone(self.list._head.next)

if __name__ == '__main__':
    unittest.main()