from abc import ABC, abstractmethod

from extensions.roguelike.models.tile_map import TileMap


class BaseTileMapGenerator(ABC):
    """
    Base class for tile map generators.
    """

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    @abstractmethod
    def generate_tile_map(self) -> TileMap:
        """
        Generate a tile map.
        """
        pass
