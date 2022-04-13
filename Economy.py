import json
import random
import discord

from discord.ext import commands

class Economy(commands.Cog):
	def __init__(self, client) -> None:
		self.kaia = client
		self.currency = "Credit"
		with open("Wealth.json", "r") as f:
			self.data = json.load(f)
			f.close()

	def commit_database(self):
		with open("Wealth.json", "w") as f:
			json.dump(self.data, f, indent = 4)
			f.close()

# ------------------------------------------------------------------------------------------------------------------------------------------------------
# Commands
# ------------------------------------------------------------------------------------------------------------------------------------------------------

	# ---------------------------------------------------------------------------
	# Balance
	# ---------------------------------------------------------------------------

	@commands.command(name = "balance", aliases = ["wealth"])
	async def wealth(self, context : commands.Context):
		executor = context.author.name.lower()
		await context.send("Wallet : {0} {2} | Bank : {1} {2}".format(self.data[executor]["wallet"], self.data[executor]["bank"], self.currency))
	
	# ---------------------------------------------------------------------------
	# Deposit
	# ---------------------------------------------------------------------------

	@commands.command(name = "deposit")
	async def deposit(self, context : commands.Context, *, amount):
		executor = context.author.name.lower()
		self.check_for_user(executor)
		wallet = self.data[executor]["wallet"]
		bank = self.data[executor]["bank"]
		print(bank)
		try:
			amount = abs(int(amount))
			if amount <= wallet:
				wallet -= amount
				bank += amount
				self.data[executor]["wallet"] = wallet
				self.data[executor]["bank"] = bank
				await context.send("Moved {0} {1} to the bank.".format(amount, self.currency))
			else:
				await context.send("Not enough to deposit.")
		except Exception as error:
			if isinstance(error, ValueError):
				if amount == "all":
					bank += wallet
					wallet -= wallet
					self.data[executor]["wallet"] = wallet
					self.data[executor]["bank"] = bank
					await context.send("Moved all {0} into the bank.".format(self.currency))
		finally:
			self.commit_database()

	# ---------------------------------------------------------------------------
	# Withdraw
	# ---------------------------------------------------------------------------

	@commands.command(name = "withdraw")
	async def withdraw(self, context : commands.Context, *, amount):
		executor = context.author.name.lower()
		self.check_for_user(executor)
		wallet = self.data[executor]["wallet"]
		bank = self.data[executor]["bank"]
		print(bank)
		try:
			amount = abs(int(amount))
			if amount <= wallet:
				wallet += amount
				bank -= amount
				self.data[executor]["wallet"] = wallet
				self.data[executor]["bank"] = bank
				await context.send("Moved {0} {1} to your wallet.".format(amount, self.currency))
			else:
				await context.send("Not enough to withdraw.")
		except Exception as error:
			if isinstance(error, ValueError):
				if amount == "all":
					wallet += bank
					bank -= bank
					self.data[executor]["wallet"] = wallet
					self.data[executor]["bank"] = bank
					await context.send("Moved all {0} to your wallet.".format(self.currency))
		finally:		
			self.commit_database()
	
	# ---------------------------------------------------------------------------
	# Gamble
	# ---------------------------------------------------------------------------

	@commands.command(name = "gamble", aliases = ["bet"])
	async def gamble(self, context : commands.Context, *, amount):
		executor = context.author.name.lower()
		self.check_for_user(executor)
		wallet = self.data[executor]["wallet"]
		try:
			amount = abs(int(amount))
			if wallet >= amount:
				gambling_rng = random.choice([0, 1])
				if gambling_rng == 0:
					wallet -= amount
					self.data[executor]["wallet"] = wallet
					await context.send("You lost! Better luck next time.")
				elif gambling_rng == 1:
					wallet += amount * 2
					self.data[executor]["wallet"] = wallet
					await context.send("You won: {0} {1}!".format(amount * 2, self.currency))
				else:
					await context.send("You don't have that much in your wallet to bet!")
		except Exception as error:
			if isinstance(error, ValueError):
				if amount == "all":
					gambling_rng = random.choice([0, 1])
					if gambling_rng == 0:
						wallet -= wallet
						self.data[executor]["wallet"] = wallet
						await context.send("You lost! Better luck next time.")
					elif gambling_rng == 1:
						wallet = wallet * 2
						self.data[executor]["wallet"] = wallet
						await context.send("You won: {0} {1}!".format(wallet * 2, self.currency))
		finally:
			self.commit_database()
	
	# ---------------------------------------------------------------------------
	# Rob
	# ---------------------------------------------------------------------------

	@commands.command(name = "rob", aliases = ["steal"])
	async def rob(self, context : commands.Context, other : discord.Member):
		executor = context.author.name.lower()
		receiver = other.name.lower()
		self.check_for_user(executor)
		self.check_for_user(receiver)
		if executor != receiver:
			executor_wallet = self.data[executor]["wallet"]
			receiver_wallet = self.data[receiver]["wallet"]
			robbery_rng = random.choice([0, 1, 2])
			if robbery_rng == 0:
				if executor_wallet != 0:
					lost_amount = random.randint(1, executor_wallet)
					executor_wallet -= lost_amount
					self.data[executor]["wallet"] = executor_wallet
					await context.send("{0} tried to rob {1} and dropped {2} {3}.".format(executor.capitalize(), receiver.capitalize(), lost_amount, self.currency))
				else:
					await context.send("{0} tried to rob {1} but failed miserably.".format(executor.capitalize(), receiver.capitalize()))
			elif robbery_rng == 1:
				if receiver_wallet >= 100:
					stolen_amount = random.randint(1, 100)
					receiver_wallet -= stolen_amount
					executor_wallet += stolen_amount
					self.data[executor]["wallet"] = executor_wallet
					self.data[receiver]["wallet"] = receiver_wallet
					await context.send("{0} robbed {1} of {2} {3}.".format(executor.capitalize(), receiver.capitalize(), stolen_amount, self.currency))
				elif receiver_wallet < 100:
					stolen_amount = random.randint(1, receiver_wallet)
					receiver_wallet -= stolen_amount
					executor_wallet += stolen_amount
					self.data[executor]["wallet"] = executor_wallet
					self.data[receiver]["wallet"] = receiver_wallet
					await context.send("{0} robbed {1} of {2} {3}.".format(executor.capitalize(), receiver.capitalize(), stolen_amount, self.currency))
			elif robbery_rng == 2:
				stolen_amount = random.randint(1, receiver_wallet)
				receiver_wallet -= stolen_amount
				executor_wallet += stolen_amount
				self.data[executor]["wallet"] = executor_wallet
				self.data[receiver]["wallet"] = receiver_wallet
				await context.send("{0} robbed {1} of {2} {3}.".format(executor.capitalize(), receiver.capitalize(), stolen_amount, self.currency))
		else:
			await context.send("Robbing yourself is pointless.")
	
	# ---------------------------------------------------------------------------
	# Give
	# ---------------------------------------------------------------------------

	@commands.command(name = "give")
	async def give(self, context : commands.Context, other : discord.Member, amount):
		executor = context.author.name.lower()
		receiver = other.name.lower()
		self.check_for_user(executor)
		self.check_for_user(receiver)
		if executor != receiver:
			executor_wallet = self.data[executor]["wallet"]
			receiver_wallet = self.data[receiver]["wallet"]
			try:
				amount = abs(int(amount))
				if executor_wallet >= amount:
					executor_wallet -= amount
					receiver_wallet += amount
					self.data[executor]["wallet"] = executor_wallet
					self.data[receiver]["wallet"] = receiver_wallet
					await context.send("{0} gave {1} {2} {3}.".format(executor.capitalize(), receiver.capitalize(), amount, self.currency))
				else:
					await context.send("You cannot give more than you have.")
			except Exception as error:
				if isinstance(error, ValueError):
					if amount == "all":
						receiver_wallet += executor_wallet
						executor_wallet -= executor_wallet
						self.data[executor]["wallet"] = executor_wallet
						self.data[receiver]["wallet"] = receiver_wallet
						await context.send("{0} gave {1} {2} {3}.".format(executor.capitalize(), receiver.capitalize(), amount, self.currency))
			finally:
				self.commit_database()

# ------------------------------------------------------------------------------------------------------------------------------------------------------
# End
# ------------------------------------------------------------------------------------------------------------------------------------------------------