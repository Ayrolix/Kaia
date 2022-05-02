import random
import sys

from discord.ext import commands
from discord.ext.commands import Context

class Misc(commands.Cog):
	def __init__(self, bot) -> None:
		self.kaia = bot

	@commands.command(name = "roll")
	async def roll(self, context: Context, num_of_dice : int, num_of_faces : int):
		results = []
		if num_of_dice <= 188:
			if num_of_faces <= 366:
				for x in range(num_of_dice):
					results.append(random.randint(1, num_of_faces))
				await context.send(f"Results: {results}")
			else:
				await context.send("Amount of faces per die surpasses limitation.")
		else:
			await context.send("Amount of dice surpasses limitation.")