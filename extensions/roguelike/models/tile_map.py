from extensions.roguelike.models.tile import Tile


class TileMap:
    """
    A class representing a tile map.
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tiles = [[Tile() for _ in range(height)] for _ in range(width)]

    def get_tile(self, x, y) -> Tile:
        if x < 0 or y < 0 or x >= self.width or y >= self.height:
            return None
        return self.tiles[x][y]

    def set_tile(self, x, y, tile):
        self.tiles[x][y] = tile

    def get_width(self) -> int:
        return self.width

    def get_height(self) -> int:
        return self.height

    def view_from(self, x: int, y: int, width: int = 15, height: int = 15) -> list[list[Tile]]:
        """
        Returns a view of the map from the given coordinates.
        """
        view = []
        for i in range(width):
            row = []
            for j in range(height):
                row.append(self.get_tile(x + i - width // 2, y + j - height // 2))
            view.append(row)
        return view
