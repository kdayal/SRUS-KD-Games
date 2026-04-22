class Player:
    """
    Represents a player within the SRU Games system.
    """

    def __init__(self, uid: str, name: str, score: int = 0):
        """
        Initializes a Player with a unique ID and a name.
        """
        self._uid = uid
        self._name = name
        self._score = score  

    @property
    def uid(self) -> str:
        return self._uid

    @property
    def name(self) -> str:
        return self._name

    
    @property
    def score(self) -> int:
        return self._score

    
    @score.setter
    def score(self, value: int):
        if value < 0:
            raise ValueError("Score must be positive")
        self._score = value

    
    def __str__(self) -> str:
        return f"ID: {self._uid} | Player: {self._name}"