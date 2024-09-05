from extensions.roguelike.models.tile import Tile
from extensions.roguelike.models.tile_map import TileMap
from extensions.roguelike.tile_map_generation.base_tile_map_generator import BaseTileMapGenerator


class SimpleTileMapGenerator(BaseTileMapGenerator):
    """
    A simple tile map generator.
    """

    def generate_tile_map(self) -> TileMap:
        """
        Generate a tile map.
        """
        tile_map = TileMap(self.width, self.height)
        for y in range(self.height):
            for x in range(self.width):
                tile_map.set_tile(x, y, Tile())
        return tile_map
