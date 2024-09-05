from utils.ansi import ANSI


class Entity:
    """
    A generic object to represent players, enemies, items, etc
    """

    def __init__(self, name: str, char: str, ansi: str = ANSI.WHITE()):
        self.name = name
        self.char = char
        self.ansi = ansi
        self.map = None

    def move(self, dx: int, dy: int) -> bool:
        return self.map.move_entity(self, dx, dy)
