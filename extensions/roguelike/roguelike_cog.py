from discord import Embed
from discord.ext import commands

from base.base_cog import BaseCog
from core.bot import MyBot
from extensions.roguelike.tile_map_generation.simple_tile_map_generator import SimpleTileMapGenerator
from utils.ansi import ANSI


class RoguelikeCog(BaseCog):
    """
    RoguelikeCog is a cog that runs the Roguelike system.
    """
    turn_timer = 10  # seconds

    def __init__(self, bot: MyBot) -> None:
        super().__init__(bot)
        self.tile_map = SimpleTileMapGenerator(100, 100).generate_tile_map()

    @commands.command("test_ansi")
    async def test_ansi(self, ctx: commands.Context, text_to_format: str):
        ansi_text = ANSI.format_ansi(text_to_format, ANSI.BG_ORANGE())
        await ctx.send("```ansi\n" + ansi_text + "\n```")

    @commands.command("test_buffer")
    async def test_buffer(self, ctx: commands.Context):
        message = ""
        for i in range(15 * 15):
            message += str(i % 10) + " "
            if i % 15 == 14:
                message += "\n"
        ansi_text = ANSI.format_ansi(message, ANSI.BG_MARBLE_BLUE())
        await ctx.send("```ansi\n" + ansi_text + "\n```")

    @commands.command("test_tile_map")
    async def test_tile_map(self, ctx: commands.Context, x: int, y: int):
        tiles = self.tile_map.view_from(x, y)
        message = ""
        for row in tiles:
            for tile in row:
                if tile is None:
                    message += "  "
                else:
                    message += str(tile) + " "
            message += "\n"

        embed = Embed(title="Tile Map", description="```ansi\n" + message + "\n```")
        await ctx.send(embed=embed)

        # python.debug.asyncio.repl


async def setup(bot):
    await bot.add_cog(RoguelikeCog(bot))


async def teardown(bot):
    await bot.remove_cog(RoguelikeCog.__name__)
