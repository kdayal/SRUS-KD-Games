from app.player_node import PlayerNode
class PlayerList:
    def __init__(self):
       
        self._head = None

    def is_empty(self):
        return self._head is None

    def insert_head(self, player):
        new_node = PlayerNode(player)
        if self.is_empty():
            self._head = new_node
        else:
            new_node.next = self._head
            self._head.prev = new_node
            self._head = new_node   