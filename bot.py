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
        print(f'[!] {self.bot.user.name} is ready!\n'
              f'Discord.py version: {discord.__version__}\n')
        example_loop.start()

    @tasks.loop(minutes=1.0)
    async def example_loop(self):
        print(f"Loop executed {loop}")
        self.loop += 1

    @commands.command(name="ping")
    async def _test_cmd(self, ctx):
        await ctx.send("Pong!")

# Run bot
client.add_cog(Template(client))
client.run(TOKEN)
