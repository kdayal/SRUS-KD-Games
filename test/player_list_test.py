def test_insert_tail(self):
        """Check if player is added to the end of the list."""
        p2 = Player("KD002", "Amit")
        self.list.insert_head(self.p1) # Khushboo (Head)
        self.list.insert_tail(p2)      # Amit (Tail)
        
        self.assertEqual(self.list._tail.player.name, "Amit")
        self.assertEqual(self.list._head.next.player.name, "Amit")