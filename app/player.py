class Player:
    """
    Represents a player within the SRU Games system.
    """

    def __init__(self, uid: str, name: str, score: int = 0):
        self._uid = uid
        self._name = name
        self._score = score

    # -------------------
    # Getters
    # -------------------
    @property
    def uid(self) -> str:
        return self._uid

    @property
    def name(self) -> str:
        return self._name

    @property
    def score(self) -> int:
        return self._score

    # -------------------
    # Setter
    # -------------------
    @score.setter
    def score(self, value: int):
        if value < 0:
            raise ValueError("Score must be positive")
        self._score = value

    # -------------------
    # String output
    # -------------------
    def __str__(self) -> str:
        return f"ID: {self._uid} | Player: {self._name}"

    def __repr__(self):
        return f"Player(uid='{self._uid}', name='{self._name}', score={self._score})"

    # -------------------
    # Sorting support 
    # -------------------
    def __lt__(self, other):
        return self.score < other.score

    def __eq__(self, other):
        return (
            self.uid == other.uid and
            self.name == other.name and
            self.score == other.score
        )

    # -------------------
    # Custom sorting (DESC)
    # -------------------
    @classmethod
    def sort_players_desc(cls, players):
        if len(players) <= 1:
            return players

        pivot = players[len(players) // 2]

        left = []
        middle = []
        right = []

        for p in players:
            if p.score > pivot.score:      # higher score → left
                left.append(p)
            elif p.score < pivot.score:    # lower score → right
                right.append(p)
            else:
                middle.append(p)           # equal scores

        return (
            cls.sort_players_desc(left)
            + middle
            + cls.sort_players_desc(right)
        )