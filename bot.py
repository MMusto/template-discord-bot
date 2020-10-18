import os, asyncio, discord
from discord.ext import commands, tasks
# Documentation : https://discordpy.readthedocs.io/en/latest/api.html

TOKEN  = os.environ["TOKEN"]
client = commands.Bot(command_prefix = '.')

class Template(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.loop = 0

    @commands.Cog.listener()
    async def on_ready(self):
        example_loop.start()

    @tasks.loop(minutes=1.0)
    async def example_loop(self):
        print(f"Loop executed {loop}")
        self.loop += 1

    @commands.command(name="ping")
    async def get_stats(self, ctx):
        await ctx.send("Pong!")

# Run bot
client.add_cog(Template(client))
client.run(TOKEN)
