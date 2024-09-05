from utils.ansi import ANSI


class Tile:
    """
    A tile on a map.
    """

    def __init__(self, passable: bool = True, char: str = '.', ansi: str = ANSI.WHITE()):
        self.passable = passable
        self.char = char
        self.ansi = ansi
        self.entity = None
        self.items = []

    def __str__(self):
        if self.entity:
            return str(self.entity)
        if self.items:
            return str(self.items[-1])
        return ANSI.format_ansi(self.char, self.ansi)
