import time
import json
import random
import discord
import requests

from discord.ext import commands
from discord import Member, Role, User
from discord.ext.commands import Cog, command, Context


class Entertainment(Cog):
	def __init__(self, client) -> None:
		self.client: commands.Bot = client
		with open("GIFS.json", "r", encoding = "utf-8") as f:
			self.urls = json.load(f)

	# ---------------------------------------------------------------------------------------------------------------------
	# GIFS
	# ---------------------------------------------------------------------------------------------------------------------

	@commands.command(name = "Slap", aliases = ["Slaps", "Slp"])
	async def slap(self, context: Context, other: str = None):
		if other is not None:
			if other.find("&") != -1:
				print("Got passed role mention check")
				selection = random.randint(0, (len(self.urls["Slaps"]) - 1))
				embed = discord.Embed(title = "*SMACK*", description = f"{context.message.author.mention} smacks everyone in {other}.", colour = discord.Colour.random(seed = time.time()))
				embed.set_image(url = str(self.urls["Slaps"][selection]))
				await context.send(embed = embed)
			else:
				if other.find("337801909417017344") != -1:
					selection = random.randint(0, (len(self.urls["Slaps"]) - 1))
					embed = discord.Embed(title = "*SMACK*", description = f"{context.message.author.mention} smacks themselves.",colour = discord.Colour.random(seed = time.time()))
					embed.set_image(url = str(self.urls["Slaps"][selection]))
					await context.send(embed = embed)
				else:
					selection = random.randint(0, (len(self.urls["Slaps"]) - 1))
					embed = discord.Embed(title = "*SMACK*", description = f"{context.message.author.mention} smacks {other}.", colour = discord.Colour.random(seed = time.time()))
					embed.set_image(url = str(self.urls["Slaps"][selection]))
					await context.send(embed = embed)
		else:
			selection = random.randint(0, (len(self.urls["Slaps"]) - 1))
			embed = discord.Embed(title = "*SMACK*", description = f"{context.message.author.mention} smacks themselves.", colour = discord.Colour.random(seed = time.time()))
			embed.set_image(url = str(self.urls["Slaps"][selection]))
			await context.send(embed = embed)

	@command(name = "hug", aliases = ["hugs", "hugz", "huggles", "embrace"])
	async def hug(self, context: Context, receiver: str = None):
		if receiver is not None:
			if receiver.find("&") == -1:
				selection = random.randint(0, (len(self.urls["Hugs"]) - 1))
				embed = discord.Embed(
					title = "*Hugs*",
					description = f"{context.message.author.mention} hugs {receiver}.",
					colour = discord.Colour.random(seed = time.time())
				)
				embed.set_image(url = str(self.urls["Hugs"][selection]))
				await context.send(embed = embed)
			else:
				selection = random.randint(0, (len(self.urls["Hugs"]) - 1))
				embed = discord.Embed(
					title = "*Hugs*",
					description = f"{context.message.author.mention} hugs everyone in {receiver}.",
					colour = discord.Colour.random(seed = time.time())
				)
				embed.set_image(url = str(self.urls["Hugs"][selection]))
				await context.send(embed = embed)
		else:
			selection = random.randint(0, (len(self.urls["Hugs"]) - 1))
			embed = discord.Embed(
				title = "*Hugs*",
				description = f"{context.message.author.mention} hugs {context.message.author.mention}.",
				colour = discord.Colour.random(seed = time.time())
			)
			embed.set_image(url = str(self.urls["Hugs"][selection]))
			await context.send(embed = embed)

	@commands.command(name = "pat", aliases = ["pats"])
	async def pats(self, context: Context, receiver: str = None):
		if receiver is not None:
			if receiver.find("&") == -1:
				selection = random.randint(0, (len(self.urls["Pats"]) - 1))
				embed = discord.Embed(
					title = "*pats*",
					description = f"{context.message.author.mention} pats {receiver}",
					colour = discord.Colour.random(seed = time.time())
				)
				embed.set_image(url = str(self.urls["Pats"][selection]))
				await context.send(embed = embed)
			else:
				selection = random.randint(0, (len(self.urls["Pats"]) - 1))
				embed = discord.Embed(
					title = "*pats*",
					description = f"{context.message.author.mention} pats everyone in {receiver}",
					colour = discord.Colour.random(seed = time.time())
				)
				embed.set_image(url = str(self.urls["Pats"][selection]))
				await context.send(embed = embed)
		elif receiver is None:
			selection = random.randint(0, (len(self.urls["Pats"]) - 1))
			embed = discord.Embed(
				title = "*pats*",
				description = f"{context.message.author.mention} pats {context.message.author.mention}",
				colour = discord.Colour.random(seed = time.time())
			)
			embed.set_image(url = str(self.urls["Pats"][selection]))
			await context.send(embed = embed)

	@commands.command(name = "pet", aliases = ["pets"])
	async def pets(self, context: Context, receiver: str = None):
		if receiver is not None:
			if receiver.find("&") == -1:
				selection = random.randint(0, (len(self.urls["Pets"]) - 1))
				embed = discord.Embed(
					title = "*pets*",
					description = f"{context.message.author.mention} pets {receiver}",
					colour = discord.Colour.random(seed = time.time())
				)
				embed.set_image(url = str(self.urls["Pets"][selection]))
				await context.send(embed = embed)
			else:
				selection = random.randint(0, (len(self.urls["Pets"]) - 1))
				embed = discord.Embed(
					title = "*pets*",
					description = f"{context.message.author.mention} pets everyone in {receiver}",
					colour = discord.Colour.random(seed = time.time())
				)
				embed.set_image(url = str(self.urls["Pets"][selection]))
				await context.send(embed = embed)
		elif receiver is None:
			selection = random.randint(0, (len(self.urls["Pets"]) - 1))
			embed = discord.Embed(
				title = "*pets*",
				description = f"{context.message.author.mention} pets {context.message.author.mention}",
				colour = discord.Colour.random(seed = time.time())
			)
			embed.set_image(url = str(self.urls["Pets"][selection]))
			await context.send(embed = embed)

	@commands.command(name = "Wuff", aliases = ["bark", "bork", "borks", "gibtreat", "brk", "treat"])
	async def wuff(self, context: Context, receiver: str = None):
		if receiver is not None:
			if receiver.find("&") == -1:
				selection = random.randint(0, (len(self.urls["Bark"]) - 1))
				embed = discord.Embed(title = "*WUFF*", description = f"{context.message.author.mention} barks at {receiver}.", colour = discord.Colour.random(seed = time.time()))
				embed.set_image(url = str(self.urls["Bark"][selection]))
				await context.send(embed = embed)
			else:
				selection = random.randint(0, (len(self.urls["Bark"]) - 1))
				embed = discord.Embed(
					title = "*WUFF*",
					description = f"{context.message.author.mention} barks at everyone in {receiver}.",colour = discord.Colour.random(seed = time.time()))
				embed.set_image(url = str(self.urls["Bark"][selection]))
				await context.send(embed = embed)
		else:
			selection = random.randint(0, (len(self.urls["Bark"]) - 1))
			embed = discord.Embed(
				title = "*WUFF*",
				description = f"{context.message.author.mention} wants a treat.",
				colour = discord.Colour.random(seed = time.time())
			)
			embed.set_image(url = str(self.urls["Bark"][selection]))
			await context.send(embed = embed)

	@commands.command(name = "givepat", aliases = ["givepats", "patnow", "givemepats"])
	async def givepats(self, context: Context):
		selection = random.randint(0, (len(self.urls["Give_Pats"]) - 1))
		embed = discord.Embed(
			title = "*Give me pats*",
			description = f"{context.message.author.mention} wants pats, NOW!.",
			colour = discord.Colour.random(seed = time.time())
		)
		embed.set_image(url = str(self.urls["Give_Pats"][selection]))
		await context.send(embed = embed)

	@commands.command(name = "Bonk", aliases = ["Bonks", "givebonks"])
	async def bonk(self, context: Context, receiver: str = None):
		if receiver is not None:
			if receiver.find("&") == -1:
				selection = random.randint(0, (len(self.urls["Bonks"]) - 1))
				embed = discord.Embed(
					title = "*Bonk*",
					description = f"{context.message.author.mention} bonks {receiver}.",
					colour = discord.Colour.random(seed = time.time())
				)
				embed.set_image(url = str(self.urls["Bonks"][selection]))
				await context.send(embed = embed)
			else:
				selection = random.randint(0, (len(self.urls["Bonks"]) - 1))
				embed = discord.Embed(
					title = "*Bonk*",
					description = f"{context.message.author.mention} bonks everyone in {receiver}.",
					colour = discord.Colour.random(seed = time.time())
				)
				embed.set_image(url = str(self.urls["Bonks"][selection]))
				await context.send(embed = embed)
		else:
			selection = random.randint(0, (len(self.urls["Bonks"]) - 1))
			embed = discord.Embed(
				title = "*Bonk*",
				description = f"{context.message.author.mention} bonks {context.message.author.mention}.",
				colour = discord.Colour.random(seed = time.time())
			)
			embed.set_image(url = str(self.urls["Bonks"][selection]))
			await context.send(embed = embed)

	@commands.command(name = "Horny", aliases = ["Hornybonk", "Hornyjail"])
	async def hbonk(self, context: Context, receiver: str = None):
		if receiver is not None:
			if receiver.find("&") == -1:
				selection = random.randint(0, 3)
				embed = discord.Embed(
					title = "*Go to horny jail.*",
					description = f"{context.message.author.mention} sends {receiver} to horny jail.",
					colour = discord.Colour.random(seed = time.time())
				)
				embed.set_image(url = str(self.urls["Horny_Bonks"][selection]))
				await context.send(embed = embed)
			else:
				selection = random.randint(0, 3)
				embed = discord.Embed(
					title = "*Go to horny jail.*",
					description = f"{context.message.author.mention} sends everyone in {receiver} to horny jail.",
					colour = discord.Colour.random(seed = time.time())
				)
				embed.set_image(url = str(self.urls["Horny_Bonks"][selection]))
				await context.send(embed = embed)
		else:
			embed = discord.Embed(
				title = "*Go to horny jail.*",
				description = f"{context.message.author.mention} sends themselves to horny jail.",
				colour = discord.Colour.random(seed = time.time())
			)
			embed.set_image(url = str(self.urls["Horny_Bonks"][4]))
			await context.send(embed = embed)

	@commands.command(name = "tailwag", aliases = ["wag", "wags", "wagging", "tailwags"])
	async def tailwag(self, context: Context):
		selection = random.randint(0, 6)
		embed = discord.Embed(
			title = "*Wags tail*",
			description = f"{context.message.author.mention} wags their tail.",
			colour = discord.Colour.random(seed = time.time())
		)
		embed.set_image(url = str(self.urls["Tail_Wag"][selection]))
		await context.send(embed = embed)

	@commands.command(name = "Boop", aliases = ["Boops", "Boopers"])
	async def boop(self, context: Context, receiver: str = None):
		if receiver is not None:
			if receiver.find("&") == -1:
				selection = random.randint(0, len(self.urls["Boops"]) - 1)
				embed = discord.Embed(
					title = "*Boop*",
					description = f"{context.message.author.mention} boops {receiver}.",
					colour = discord.Colour.random(seed = time.time())
				)
				embed.set_image(url = str(self.urls["Boops"][selection]))
				await context.send(embed = embed)
			else:
				selection = random.randint(0, len(self.urls["Boops"]) - 1)
				embed = discord.Embed(
					title = "*Boop*",
					description = f"{context.message.author.mention} boops everyone in {receiver}.",
					colour = discord.Colour.random(seed = time.time())
				)
				embed.set_image(url = str(self.urls["Boops"][selection]))
				await context.send(embed = embed)
		else:
			selection = random.randint(0, len(self.urls["Boops"]) - 1)
			embed = discord.Embed(
				title = "*Boop*",
				description = f"{context.message.author.mention} boops themselves.",
				colour = discord.Colour.random(seed = time.time())
			)
			embed.set_image(url = str(self.urls["Boops"][selection]))
			await context.send(embed = embed)

	# ---------------------------------------------------------------------------------------------------------------------
	# Images
	# ---------------------------------------------------------------------------------------------------------------------

	@commands.command(name = "floof")
	async def floofy(self, context: Context):
		response = requests.get("https://randomfox.ca/floof").json()
		embed = discord.Embed(title = "Floofy!")
		embed.set_image(url = response["image"])
		await context.send(embed = embed)

	@commands.command(name = "doggo")
	async def doggo(self, context: Context):
		response = requests.get("https://random.dog/woof.json").json()
		embed = discord.Embed(title = "Woof Woof!!")
		embed.set_image(url = response["url"])
		await context.send(embed = embed)

	@commands.command(name = "ducky")
	async def ducky(self, context: Context):
		response = requests.get("https://random-d.uk/api/v2/random").json()
		embed = discord.Embed(title = "Quackity Quack!!")
		embed.set_image(url = response["url"])
		await context.send(embed = embed)