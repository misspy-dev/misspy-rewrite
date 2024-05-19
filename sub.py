import misspy

class Test(misspy.Cog):
    def __init__(self, bot: misspy.Bot) -> None:
        self.bot = bot

    @misspy.Cog.listener("ready")
    async def rd(self):
        print("logged in: @" + self.bot.user.username)
        await self.bot.connect(misspy.Timeline.LOCAL)

async def setup(bot: misspy.Bot):
    await bot.add_cog(Test(bot))