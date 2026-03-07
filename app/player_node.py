from app.player import Player

class PlayerNode:
    def __init__(self, player: Player):
        """
        Step 4b: Initialize the node with a player object.
        Initializes next and prev pointers to None.
        """
        self._player = player
        self._next = None
        self._prev = None

    @property
    def player(self):
        """Returns the player object stored in this node."""
        return self._player

    @property
    def next(self):
        """Getter for the next node."""
        return self._next

    @next.setter
    def next(self, node):
        """Setter for the next node."""
        self._next = node

    @property
    def prev(self):
        """Getter for the previous node."""
        return self._prev

    @prev.setter
    def prev(self, node):
        """Setter for the previous node."""
        self._prev = node

    @property
    def key(self):
        """
        Step 4d: Returns the unique ID of the player.
        This makes it easy to search for a specific node.
        """
        return self._player.uid

    def __str__(self):
        """Step 4e: Human-readable string for the node."""
        return f"Node contains: {self._player}"