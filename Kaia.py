import discord

from Misc import Misc
from Economy import Economy
from discord.ext import commands
from Entertainment import Entertainment

class Client(commands.Bot):
	def __init__(self):
		super().__init__(command_prefix = "$", case_insensitive = True, intents = discord.Intents.all())

	async def on_command_error(self, context, exception):
		if isinstance(exception, commands.CommandNotFound):
			await context.send("Command not found!")
		elif isinstance(exception, commands.CommandOnCooldown):
			await context.send("Command is on cooldown! Be patient.")

if __name__ == "__main__":
	Kaia = Client()
	Kaia.add_cog(Entertainment(Kaia))
	Kaia.add_cog(Economy(Kaia))
	Kaia.add_cog(Misc(Kaia))
	Kaia.run()
