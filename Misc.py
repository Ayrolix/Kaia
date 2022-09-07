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
		if num_of_dice > 188:
			await context.send("You cannot roll more than 188 dice.")
			return
		if num_of_faces > 366:
			await context.send("You cannot roll dice with more than 366 faces.")
			return
		for i in range(num_of_dice):
			results.append(random.randint(1, num_of_faces))
		await context.send(results)