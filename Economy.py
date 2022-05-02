import random

from Types.data_types import *
from discord.ext import commands
from discord import Embed, Member
from discord.ext.commands import Cog, Context, BucketType


class Economy(Cog):
	def __init__(self, client):
		self.kaia = client
		self.currency_name = "Credits"
		self.data = Database("Wealth.json")
		self.cache_data = []
		self.beta_state = 0
		self.owner_id = 337801909417017344

	@commands.command(name = "beta", hidden = True)
	async def beta_mode(self, context: Context, *, mode: int):
		if int(context.author.id) == self.owner_id:
			username = context.author.name.lower()
			user = self.data.pull_user(username)
			mode = abs(mode)
			if mode == 0:
				if self.beta_state != 0:
					self.beta_state = 0
					user.wallet = self.cache_data[0]
					user.bank = self.cache_data[1]
					self.data.commit_user(user)
					await context.send("Beta mode turned off.")
				else:
					await context.send("You can't turn off beta mode more than once.")
			elif mode == 1:
				if self.beta_state != 1:
					self.beta_state = 1
					self.cache_data.clear()
					self.cache_data.append(user.wallet)
					self.cache_data.append(user.bank)
					user.wallet = 0
					user.bank = float("inf")
					self.data.commit_user(user)
					await context.send("Beta mode turned on!")
				else:
					await context.send("You can't turn on beta mode more than once.")
			else:
				await context.send("Beta mode only has on (1) or off (0).")
			self.data.commit_data()
		else:
			await context.send("Access denied!")

	@commands.command(name = "grant", hidden = True)
	async def grant(self, context: Context, other: Member, amount):
		if int(context.author.id) == self.owner_id:
			user = self.data.pull_user(other.name.lower())
			amount = abs(int(amount))
			user.bank += amount
			self.data.commit_user(user)
			self.data.commit_data()
			await context.send(f"Owner granted {user.username.capitalize()} {amount} {self.currency_name}.")
		else:
			await context.send("Access denied!")

	@commands.command(name = "seize", hidden = True)
	async def seize(self, context: Context, other: Member, amount):
		if int(context.author.id) == self.owner_id:
			user = self.data.pull_user(other.name.lower())
			amount = abs(int(amount))
			if user.wallet >= amount:
				user.wallet -= amount
				self.data.commit_user(user)
				await context.send(f"Owner seized {amount} from {user.username.capitalize()}.")
			elif user.bank >= amount:
				user.bank -= amount
				self.data.commit_user(user)
				await context.send(f"Owner seized {amount} from {user.username.capitalize()}.")
			elif (user.wallet + user.bank) >= amount:
				user.bank += user.wallet
				user.wallet -= user.wallet
				user.bank -= amount
				self.data.commit_user(user)
				await context.send(f"Owner seized {amount} from {user.username.capitalize()}.")
			else:
				await context.send("User is poor enough! No seizing!")
			self.data.commit_data()
		else:
			await context.send("Access denied!")

	@commands.command(name = "work")
	@commands.cooldown(1, 10, BucketType.user)
	async def work(self, context: Context):
		user = self.data.pull_user(context.author.name.lower())
		earned = random.randint(20, 120)
		user.wallet += earned
		self.data.commit_user(user)
		await context.send(f"{user.username.capitalize()} earned {earned} {self.currency_name}!")
		self.data.commit_data()

	@commands.command(name = "balance")
	async def balance(self, context: Context, *, other: Member = None):
		if other is not None:
			target = self.data.pull_user(other.name.lower())
			embed = Embed(title = f"{target.username.capitalize()}", description = f"Wallet: {target.wallet} \nBank: {target.bank}")
			await context.send(embed = embed)
		else:
			user = self.data.pull_user(context.author.name.lower())
			embed = Embed(title = user.username.capitalize(), description = f"Wallet: {user.wallet} \nBank: {user.bank}")
			await context.send(embed = embed)

	@commands.command(name = "deposit")
	async def deposit(self, context: Context, *, amount):
		user = self.data.pull_user(context.author.name.lower())
		try:
			amount = abs(int(amount))
			if amount <= user.wallet:
				user.wallet -= amount
				user.bank += amount
				self.data.commit_user(user)
				await context.send(f"Moved {amount} {self.currency_name} into the bank.")
			else:
				await context.send("Not enough in your wallet to deposit.")
		except Exception as error:
			if isinstance(error, ValueError) and amount == "all":
				user.bank += user.wallet
				user.wallet = 0
				self.data.commit_user(user)
				await context.send(f"Moved all {self.currency_name} into the bank.")
		finally:
			self.data.commit_data()

	@commands.command(name = "withdraw")
	async def withdraw(self, context: Context, *, amount):
		user = self.data.pull_user(context.author.name.lower())
		try:
			amount = abs(int(amount))
			if amount <= user.bank:
				user.bank -= amount
				user.wallet += amount
				self.data.commit_user(user)
				await context.send(f"Moved {amount} {self.currency_name} to your wallet.")
			else:
				await context.send("Not enough in the bank to withdraw.")
		except Exception as error:
			if isinstance(error, ValueError) and amount == "all":
				user.wallet += user.bank
				user.bank = 0
				self.data.commit_user(user)
				await context.send(f"Moved all {self.currency_name} to your wallet.")
		finally:
			self.data.commit_data()

	@commands.command(name = "gamble")
	async def gamble(self, context: Context, *, amount):
		user = self.data.pull_user(context.author.name.lower())
		try:
			amount = abs(int(amount))
			if amount <= user.wallet:
				luck = random.choices([0, 1, 2], [45, 45, 10], k = 1)
				if luck[0] == 0:
					user.wallet -= amount
					self.data.commit_user(user)
					await context.send("You lost. Better luck next time.")
				elif luck[0] == 1:
					user.wallet += amount
					self.data.commit_user(user)
					await context.send(f"Congratulations. You won {amount * 2} {self.currency_name}.")
				elif luck[0] == 2:
					user.wallet += (amount << 5)
					self.data.commit_user(user)
					await context.send(f"Congratulations. You won {amount << 5} {self.currency_name}.")
			else:
				await context.send("Don't have that much to gamble.")
		except Exception as error:
			if isinstance(error, ValueError) and amount == "all":
				luck = random.choices([0, 1, 2], [45, 45, 10], k = 1)
				if luck[0] == 0:
					user.wallet -= user.wallet
					self.data.commit_user(user)
					await context.send("You lost. Better luck next time.")
				elif luck[0] == 1:
					user.wallet += user.wallet
					self.data.commit_user(user)
					await context.send(f"Congratulations. You won {user.wallet * 2} {self.currency_name}.")
				elif luck[0] == 2:
					user.wallet += (user.wallet << 5)
					self.data.commit_user(user)
					await context.send(f"Congratulations. You won {user.wallet << 5} {self.currency_name}.")
					print("jackpot")
		finally:
			self.data.commit_data()

	@commands.command(name = "rob")
	async def rob(self, context: Context, other: Member):
		robber = self.data.pull_user(context.author.name.lower())
		victim = self.data.pull_user(other.name.lower())
		if robber.username != victim.username:
			luck = random.choices([0, 1, 2], [45, 45, 10], k = 1)
			if luck[0] == 0:
				if robber.wallet != 0:
					amount_lost = random.randint(1, robber.wallet)
					robber.wallet -= amount_lost
					self.data.commit_user(robber)
					await context.send(f"{robber.username.capitalize()} tried to rob {victim.username.capitalize()} and dropped {amount_lost} {self.currency_name}.")
					self.data.commit_data()
				else:
					await context.send(f"{robber.username.capitalize()} tried to rob {victim.username.capitalize()} but failed miserably.")
			elif luck[0] == 1:
				if victim.wallet > 100:
					amount_stolen = random.randint(1, 100)
					victim.wallet -= amount_stolen
					robber.wallet += amount_stolen
					self.data.commit_user(robber) ; self.data.commit_user(victim)
					await context.send(f"{robber.username.capitalize()} robbed {victim.username.capitalize()} of {amount_stolen} {self.currency_name}.")
					self.data.commit_data()
				else:
					amount_stolen = random.randint(1, victim.wallet)
					robber.wallet += amount_stolen
					victim.wallet -= amount_stolen
					self.data.commit_user(robber) ; self.data.commit_user(victim)
					await context.send(f"{robber.username.capitalize()} robbed {victim.username.capitalize()} of {amount_stolen} {self.currency_name}.")
					self.data.commit_data()
			elif luck[0] == 2:
				amount_stolen = random.randint(1, victim.wallet)
				robber.wallet += amount_stolen
				victim.wallet -= amount_stolen
				self.data.commit_user(robber) ; self.data.commit_user(victim)
				await context.send(f"{robber.username.capitalize()} robbed {victim.username.capitalize()} of {amount_stolen} {self.currency_name}.")
				self.data.commit_data()

	@commands.command(name = "give")
	async def give(self, context: Context, other: Member, amount):
		giver = self.data.pull_user(context.author.name.lower())
		receiver = self.data.pull_user(other.name.lower())
		if giver.username != receiver.username:
			try:
				amount = abs(int(amount))
				if giver.wallet >= amount:
					giver.wallet -= amount
					receiver.wallet += amount
					self.data.commit_user(giver) ; self.data.commit_user(receiver)
					await context.send(f"{giver.username.capitalize()} gave {receiver.username.capitalize()} {amount} {self.currency_name}.")
				else:
					await context.send("You cannot give more than you have.")
			except Exception as error:
				if isinstance(error, ValueError) and amount == "all":
					receiver.wallet += giver.wallet
					giver.wallet = 0
					self.data.commit_user(giver) ; self.data.commit_user(receiver)
					await context.send(f"{giver.username.capitalize()} gave {receiver.username.capitalize()} all their {self.currency_name}.")
			finally:
				self.data.commit_data()