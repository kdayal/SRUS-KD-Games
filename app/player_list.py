from app.player_node import PlayerNode

class PlayerList:
    def __init__(self):
        """Initializes the list with head and tail as None."""
        self._head = None
        self._tail = None

    def is_empty(self):
        """Returns True if the list is empty."""
        return self._head is None

    def insert_head(self, player):
        """Inserts a new player at the beginning of the list."""
        new_node = PlayerNode(player)
        if self.is_empty():
            self._head = self._tail = new_node
        else:
            new_node.next = self._head
            self._head.prev = new_node
            self._head = new_node 

    def insert_tail(self, player):
        """Inserts a new player at the end of the list."""
        new_node = PlayerNode(player)
        if self.is_empty():
            self._head = self._tail = new_node
        else:
            new_node.prev = self._tail
            self._tail.next = new_node
            self._tail = new_node

    def delete_head(self):
        """Step 7d: Deletes the node at the beginning of the list."""
        if self.is_empty():
            return

        if self._head == self._tail:
            self._head = self._tail = None
        else:
            self._head = self._head.next
            self._head.prev = None

    def delete_tail(self):
        """Step 7d: Deletes the node at the end of the list."""
        if self.is_empty():
            return

        if self._head == self._tail:
            self._head = self._tail = None
        else:
            self._tail = self._tail.prev
            self._tail.next = None

    def delete_by_key(self, key):
        """Step 7g: Finds and deletes a player by their UID (key)."""
        current = self._head
        while current:
            if current.key == key:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self._head = current.next

                if current.next:
                    current.next.prev = current.prev
                else:
                    self._tail = current.prev
                return True 
            current = current.next
        return False

    def display(self, forward=True):
        """Step 8: Traverses and prints the list."""
        if self.is_empty():
            print("The list is empty.")
            return

        current = self._head if forward else self._tail
        print(f"--- Displaying List ({'Forward' if forward else 'Backward'}) ---")
        while current:
            print(current)
            current = current.next if forward else current.prev