from base.base_cog import BaseCog
from core.bot import MyBot


class RoguelikeCog(BaseCog):
    """
    RoguelikeCog is a cog that runs the Roguelike system.
    """

    def __init__(self, bot: MyBot) -> None:
        super().__init__(bot)


async def setup(bot):
    await bot.add_cog(RoguelikeCog(bot))


async def teardown(bot):
    await bot.remove_cog(RoguelikeCog.__name__)
