import discord
from discord.ext import commands
from GIFS import GIFS

class Client(commands.Bot):
	def __init__(self):
		super().__init__(command_prefix = "$", case_insensitive = True, intents = discord.Intents.all())

if __name__ == "__main__":
	Kaia = Client()
	Kaia.add_cog(GIFS(Kaia))
	Kaia.run("NzUxNjMwNDQ1MjI5MTEzNDY0.X1L4Zg.qVUgIdentp-gaenoG6RH44K6EsU")