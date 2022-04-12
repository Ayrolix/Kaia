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
	
	def save_database(self) -> None:
		with open("Wealth.json", "w") as f:
			json.dump(self.data, f, indent = 4)

	def get_wallet(self, user_id):
		return self.data[user_id]["wallet"]

	def get_bank(self, user_id):
		return self.data[user_id]["bank"]

	def set_wallet(self, user_id, amount):
		self.data[user_id]["wallet"] = amount
	
	def set_bank(self, user_id, amount):
		self.data[user_id]["bank"] = amount
	
	def set_user(self, user_id):
		if user_id not in self.data:
			self.data[user_id] = {"wallet" : 0, "bank" : 5000, "inventory" : []}
			pass
		else:
			pass

# ------------------------------------------------------------------------------------------------------------------------------------------------------
# Commands
# ------------------------------------------------------------------------------------------------------------------------------------------------------

	# ---------------------------------------------------------------------------
	# Balance
	# ---------------------------------------------------------------------------

	@commands.command(name = "balance")
	async def balance(self, context):
		user = str(context.author.id)
		self.set_user(user)
		wallet, bank = self.get_wallet(user), self.get_bank(user)
		await context.send(f"Wallet: {wallet}, Bank: {bank}.")
	
	# ---------------------------------------------------------------------------
	# Deposit
	# ---------------------------------------------------------------------------

	@commands.command(name = "deposit")
	async def deposit(self, context, *, amount):
		user = str(context.author.id)
		self.set_user(user)
		wallet, bank = self.get_wallet(user), self.get_bank(user)
		try:
			amount = abs(int(amount))
			if amount <= wallet:
				wallet -= amount ; bank += amount
				self.data[user].update({"wallet": wallet, "bank": bank})
				await context.send(f"Successfully moved {amount} {self.currency}s to your bank!")
			else:
				await context.send("You don't have enough to deposit into your bank.")
		except Exception as err:
			if isinstance(err, ValueError):
				if amount == "all":
					bank += wallet ; wallet -= wallet
					self.data[user].update({"wallet": wallet, "bank": bank})
					await context.send(f"Successfully moved all {self.currency}s to your bank!")
		finally:
			self.save_database()		

	# ---------------------------------------------------------------------------
	# Withdraw
	# ---------------------------------------------------------------------------

	@commands.command(name = "withdraw")
	async def withdraw(self, context, *, amount):
		user = str(context.author.id)
		self.set_user(user)
		wallet, bank = self.get_wallet(user), self.get_bank(user)
		try:
			amount = abs(int(amount))
			if amount <= bank:
				wallet += amount ; bank -= amount
				self.data[user].update({"wallet": wallet, "bank": bank})
				await context.send(f"Successfully moved {amount} {self.currency}s to your wallet!")
			else:
				await context.send("You don't have enough to withdraw from your bank.")
		except Exception as err:
			if isinstance(err, ValueError):
				if amount == "all":
					wallet += bank ; bank -= bank;
					self.data[user].update({"wallet": wallet, "bank": bank})
					await context.send(f"Successfully moved all {self.currency}s to your wallet!")
		finally:
			self.save_database()
	
	# ---------------------------------------------------------------------------
	# Gamble
	# ---------------------------------------------------------------------------

	@commands.command(name = "gamble")
	async def gamble(self, context, *, amount):
		user = str(context.author.id)
		self.set_user(user)
		wallet = self.get_wallet(user)
		try:
			amount = abs(int(amount))
			if wallet >= amount:
				luck = random.choices([0, 1, 2], [75, 50, 1], k = 1)[0]
				if luck == 0:
					wallet -= amount
					self.data[user].update({"wallet": wallet})
					await context.send("You lost! Better luck next time.")
				elif luck == 1:
					wallet += amount * 2
					self.data[user].update({"wallet": wallet})
					await context.send(f"You won {amount * 2} {self.currency}s!")
				elif luck == 2:
					wallet += amount ** 2
					self.data[user].update({"wallet": wallet})
					await context.send(f"Lucky individual aren't you {context.author.name}! You won {amount ** 2} {self.currency}s!")
			else:
				await context.send("You don't have that much in your wallet to bet!")
		except Exception as err:
			if isinstance(err, ValueError):
				if amount == "all":
					luck = random.choices([0, 1, 2], [75, 50, 1], k = 1)[0]
					if luck == 0:
						wallet -= wallet
						self.data[user].update({"wallet": wallet})
						await context.send("You lost! Better luck next time.")
					elif luck == 1:
						wallet += wallet * 2
						self.data[user].update({"wallet": wallet})
						await context.send(f"You won {wallet * 2} {self.currency}s!")
					elif luck == 2:
						wallet += wallet ** 2
						self.data[user].update({"wallet": wallet})
						await context.send(f"Lucky individual aren't you {context.author.name}! You won {wallet ** 2} {self.currency}s!")
		finally:
			self.save_database()
	
	# ---------------------------------------------------------------------------
	# Rob
	# ---------------------------------------------------------------------------

	@commands.command(name = "rob")
	async def rob(self, context : commands.Context, victim : discord.Member):
		robber_id = str(context.author.id), 
		victim_id = str(victim.id)
		self.set_user(robber_id)
		self.set_user(victim_id)
		r_wallet = self.get_wallet(robber_id)
		v_wallet = self.get_wallet(victim_id)
		try:
			luck = random.choices([0, 1, 2], [75, 50, 1], k = 1)[0]
			if luck == 0:
				if r_wallet != 0:
					if r_wallet > 100:
						dropped = random.randint(1, 100)
						r_wallet -= dropped
						self.data[robber_id].update({"wallet": r_wallet})
						await context.send(f"{context.author.name} underestimated {victim.name} and dropped {dropped} {self.currency}s trying to get away.")
					else:
						dropped = random.randint(1, r_wallet)
						r_wallet -= dropped
						self.data[robber_id].update({"wallet": r_wallet})
						await context.send(f"{context.author.name} underestimated {victim.name} and dropped {dropped} {self.currency}s trying to get away.")
				else:
					await context.send(f"{context.author.name} tried robbing <@{victim_id}> but it didn't go according to plan.")
			elif luck == 1:
				if v_wallet != 0:
					if v_wallet > 100:
						stolen = random.randint(1, 100)
						v_wallet -= stolen
						r_wallet += stolen
						self.data[victim_id].update({"wallet": v_wallet})
						self.data[robber_id].update({"wallet": r_wallet})
						await context.send(f"{context.author.name} stole {stolen} from <@{victim_id}>.")
					else: # In case v_wallet is less than 100
						stolen = random.randint(1, v_wallet)
						v_wallet -= stolen
						r_wallet += stolen
						self.data[victim_id].update({"wallet": v_wallet})
						self.data[robber_id].update({"wallet": r_wallet})
						await context.send(f"{context.author.name} stole {stolen} from <@{victim_id}>.")
				else:
					await context.send(f"{context.author.name} tried robbing <@{victim_id}> but their either broke or smart.")
			elif luck == 2:
				if v_wallet != 0:
					stolen = random.randint(1, v_wallet)
					v_wallet -= stolen ; r_wallet += stolen
					self.data[victim_id].update({"wallet": v_wallet})
					self.data[robber_id].update({"wallet": r_wallet})
					await context.send(f"It was not <@{victim_id}>'s lucky day. {context.author.name} stole {stolen} {self.currency}s.")
				else:
					await context.send(f"{context.author.name} tried robbing <@{victim_id}> but their either broke or smart.")
		except Exception as err:
			print(err)
		finally:
			self.save_database()
	
	# ---------------------------------------------------------------------------
	# Give
	# ---------------------------------------------------------------------------

	@commands.command(name = "give")
	async def give(self, context, reciever : discord.Member):
		giver_id = str(context.author.id)
		reciever_id = str(reciever.id)
		self.set_user(giver_id)
		self.set_user(reciever_id)
		g_wallet = self.get_wallet(giver_id)
		r_wallet = self.get_wallet(reciever_id)
		try:
			amount = abs(int(amount))
			if g_wallet >= amount:
				r_wallet += amount
				g_wallet -= amount
				self.data[giver_id].update({"wallet": g_wallet})
				self.data[reciever_id].update({"wallet": r_wallet})
				await context.send(f"{context.author.name} successfully gave {reciever.name} {amount} {self.currency}s!")
			else:
				await context.send("You cannot give more than you have!")
		except Exception as err:
			if isinstance(err, ValueError):
				if amount == "all":
					r_wallet += g_wallet
					g_wallet -= g_wallet
					self.data[giver_id].update({"wallet": g_wallet})
					self.data[reciever_id].update({"wallet": r_wallet})
					await context.send(f"{context.author.name} successfully gave {reciever.name} all their {self.currency}s!")
		finally:
			self.save_database()

# ------------------------------------------------------------------------------------------------------------------------------------------------------
# End
# ------------------------------------------------------------------------------------------------------------------------------------------------------