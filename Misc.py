import discord
import random

from discord.ext import commands

class Misc:
	def __init__(self, bot) -> None:
		self.kaia = bot

	@commands.command(name = "roll")
	async def roll(self, context: commands.Context, num_of_dice, num_of_faces):
		results = []
		for x in range(num_of_dice):
			results.append(random.randint(1, num_of_faces))
		await context.send(f"You roll results are: {results}")