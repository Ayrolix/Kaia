import discord

from GIFS import GIFS
from Economy import Economy
from discord.ext import commands

class Client(commands.Bot):
	def __init__(self):
		super().__init__(command_prefix = "$", case_insensitive = True, intents = discord.Intents.all())

if __name__ == "__main__":
	Kaia = Client()
	Kaia.add_cog(GIFS(Kaia))
	Kaia.add_cog(Economy(Kaia))
	Kaia.run()