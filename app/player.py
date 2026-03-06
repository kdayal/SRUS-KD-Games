class Player:
    """
    Represents a player within the SRU Games system.
    """

    def __init__(self, uid: str, name: str):
        """
        Initializes a Player with a unique ID and a name.
        :param uid: A unique string identifier for the player.
        :param name: The display name of the player.
        """
        self._uid = uid
        self._name = name

    @property
    def uid(self) -> str:
        """Returns the unique identifier of the player."""
        return self._uid

    @property
    def name(self) -> str:
        """Returns the name of the player."""
        return self._name

    def __str__(self) -> str:
        """Returns a human-readable string representation of the player."""
        return f"ID: {self._uid} | Player: {self._name}"