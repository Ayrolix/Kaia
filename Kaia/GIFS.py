import time
import json
import random
import discord
import logging
from discord.enums import NotificationLevel
from discord.ext import commands
from discord.ext.commands.core import has_role

'''if member is not None:
			selection = random.randint(0, 29)
			Embed = discord.Embed(title = "Hugs!", description = f"{context.message.author.mention} hugs {member.mention}", colour = discord.Colour.random(seed = time.time()))
			Embed.set_image(url = str(self.urls["Hugs"][selection]))
			logging.info(f"Hug Link Slot: #{selection}")
			await context.send(embed = Embed)
		elif member is None:
			selection = random.randint(0, 29)
			Embed = discord.Embed(title = "Hugs!", description = f"{context.message.author.mention} hugs {context.message.author.mention}", colour = discord.Colour.random(seed = time.time()))
			Embed.set_image(url = str(self.urls["Hugs"][selection]))
			await context.send(embed = Embed)'''

EMPEROR_ID = 226358815317032960
OWNER_ID = 337801909417017344
HERMES_ID = 392658397536976908
COPEN_ID = 410247463300235276

class GIFS(commands.Cog):
	def __init__(self, client) -> None:
		self.client : commands.Bot = client
		self.creators : list = [392658397536976908, 337801909417017344, 410247463300235276]
		with open("Actions/Blep.json", "r", encoding = "utf-8") as f:
			self.urls = json.load(f)

# ------------------------------------------------------------------------------------------------------------------------------------------------------
# Hug
# ------------------------------------------------------------------------------------------------------------------------------------------------------

	@commands.has_role(912542628699070495)
	@commands.command(name = "hug", aliases = ["hugs", "hugz", "huggles", "embrace"])
	async def Hug(self, context : commands.Context, reciever : str = None, choice : int = None):
		if reciever is not None:
			if reciever.find("&") == -1:
				selection = random.randint(0, (len(self.urls["Hugs"]) - 1))
				Embed = discord.Embed(title = "*Hugs*", description = f"{context.message.author.mention} hugs {reciever}.", colour = discord.Colour.random(seed = time.time()))
				Embed.set_image(url = str(self.urls["Hugs"][selection]))
				await context.send(embed = Embed)
			else: 
				selection = random.randint(0, (len(self.urls["Hugs"]) - 1))
				Embed = discord.Embed(title = "*Hugs*", description = f"{context.message.author.mention} hugs everyone in {reciever}.", colour = discord.Colour.random(seed = time.time()))
				Embed.set_image(url = str(self.urls["Hugs"][selection]))
				await context.send(embed = Embed)
		else:
			selection = random.randint(0, (len(self.urls["Hugs"]) - 1))
			Embed = discord.Embed(title = "*Hugs*", description = f"{context.message.author.mention} hugs {context.message.author.mention}.", colour = discord.Colour.random(seed = time.time()))
			Embed.set_image(url = str(self.urls["Hugs"][selection]))
			await context.send(embed = Embed)

# ------------------------------------------------------------------------------------------------------------------------------------------------------
# Slap
# ------------------------------------------------------------------------------------------------------------------------------------------------------

	@commands.command(name = "Slap", aliases = ["Slaps", "Slp"])
	async def Slap(self, context : commands.Context, reciever : str = None):
		if reciever is not None:
			if reciever.find("&") == -1:
				selection = random.randint(0, (len(self.urls["Slaps"]) - 1))
				Embed = discord.Embed(title = "*SMACK*", description = f"{context.message.author.mention} smacks {reciever}", colour = discord.Colour.random(seed = time.time()))
				Embed.set_image(url = str(self.urls["Slaps"][selection]))
				await context.send(embed = Embed)
			else:
				selection = random.randint(0, (len(self.urls["Slaps"]) - 1))
				Embed = discord.Embed(title = "*SMACK*", description = f"{context.message.author.mention} smacks everyone in {reciever}", colour = discord.Colour.random(seed = time.time()))
				Embed.set_image(url = str(self.urls["Slaps"][selection]))
				await context.send(embed = Embed)
		elif reciever is None:
			selection = random.randint(0, (len(self.urls["Slaps"]) - 1))
			Embed = discord.Embed(title = "*SMACK*", description = f"{context.message.author.mention} smacks {context.message.author.mention}", colour = discord.Colour.random(seed = time.time()))
			Embed.set_image(url = str(self.urls["Slaps"][selection]))
			await context.send(embed = Embed)

# ------------------------------------------------------------------------------------------------------------------------------------------------------
# Pats
# ------------------------------------------------------------------------------------------------------------------------------------------------------

	@commands.command(name = "Pats", aliases = ["pat"])
	async def Pats(self, context : commands.Context, reciever : str = None):
		if reciever is not None:
			if reciever.find("&") == -1:
				selection = random.randint(0, (len(self.urls["Pats"]) - 1))
				Embed = discord.Embed(title = "*pats*", description = f"{context.message.author.mention} pats {reciever}", colour = discord.Colour.random(seed = time.time()))
				Embed.set_image(url = str(self.urls["Pats"][selection]))
				await context.send(embed = Embed)
			else:
				selection = random.randint(0, (len(self.urls["Pats"]) - 1))
				Embed = discord.Embed(title = "*pats*", description = f"{context.message.author.mention} pats everyone in {reciever}", colour = discord.Colour.random(seed = time.time()))
				Embed.set_image(url = str(self.urls["Pats"][selection]))
				await context.send(embed = Embed)
		elif reciever is None:
			chances = random.choices([0,1], [100,1], k = 1)[0]
			if chances == 0:
				selection = random.randint(0, (len(self.urls["Pats"]) - 1))
				Embed = discord.Embed(title = "*pats*", description = f"{context.message.author.mention} pats {context.message.author.mention}", colour = discord.Colour.random(seed = time.time()))
				Embed.set_image(url = str(self.urls["Pats"][selection]))
				await context.send(embed = Embed)
			elif chances == 1:
				creator = random.choice(self.creators)[0]
				selection = random.randint(0, (len(self.urls["Pats"]) - 1))
				Embed = discord.Embed(title = "*pats*", description = f"{context.message.author.mention} pats <@{creator}>", colour = discord.Colour.random(seed = time.time()))
				Embed.set_image(url = str(self.urls["Pats"][selection]))
				await context.send(embed = Embed)

# ------------------------------------------------------------------------------------------------------------------------------------------------------
# Pets
# ------------------------------------------------------------------------------------------------------------------------------------------------------

	@commands.command(name = "Pets", aliases = ["Pet"])
	async def Pets(self, context : commands.Context, reciever : str = None):
		if reciever is not None:
			if reciever.find("&") == -1:
				selection = random.randint(0, (len(self.urls["Pets"]) - 1))
				Embed = discord.Embed(title = "*pets*", description = f"{context.message.author.mention} pets {reciever}", colour = discord.Colour.random(seed = time.time()))
				Embed.set_image(url = str(self.urls["Pets"][selection]))
				await context.send(embed = Embed)
			else:
				selection = random.randint(0, (len(self.urls["Pets"]) - 1))
				Embed = discord.Embed(title = "*pets*", description = f"{context.message.author.mention} pets everyone in {reciever}", colour = discord.Colour.random(seed = time.time()))
				Embed.set_image(url = str(self.urls["Pets"][selection]))
				await context.send(embed = Embed)
		elif reciever is None:
			chances = random.choices([0,1], [100,1], k = 1)[0]
			if chances == 0:
				selection = random.randint(0, (len(self.urls["Pets"]) - 1))
				Embed = discord.Embed(title = "*pets*", description = f"{context.message.author.mention} pets {context.message.author.mention}", colour = discord.Colour.random(seed = time.time()))
				Embed.set_image(url = str(self.urls["Pets"][selection]))
				await context.send(embed = Embed)
			elif chances == 1:
				creator = random.choice(self.creators)[0]
				selection = random.randint(0, (len(self.urls["Pets"]) - 1))
				Embed = discord.Embed(title = "*pets*", description = f"{context.message.author.mention} pets <@{creator}>", colour = discord.Colour.random(seed = time.time()))
				Embed.set_image(url = str(self.urls["Pets"][selection]))
				await context.send(embed = Embed)

# ------------------------------------------------------------------------------------------------------------------------------------------------------
# Wuff
# ------------------------------------------------------------------------------------------------------------------------------------------------------

	@commands.command(name = "Wuff", aliases = ["bark", "bork", "borks", "gibtreat", "brk", "treat"])
	async def Wuff(self, context : commands.Context,  reciever : str = None):
		if reciever is not None:
			if reciever.find("&") == -1:
				selection = random.randint(0, (len(self.urls["Bark"]) - 1))
				Embed = discord.Embed(title = "*WUFF*", description = f"{context.message.author.mention} barks at {reciever}.", colour = discord.Colour.random(seed = time.time()))
				Embed.set_image(url = str(self.urls["Bark"][selection]))
				await context.send(embed = Embed)
			else:
				selection = random.randint(0, (len(self.urls["Bark"]) - 1))
				Embed = discord.Embed(title = "*WUFF*", description = f"{context.message.author.mention} barks at everyone in {reciever}.", colour = discord.Colour.random(seed = time.time()))
				Embed.set_image(url = str(self.urls["Bark"][selection]))
				await context.send(embed = Embed)
		else:
			selection = random.randint(0, (len(self.urls["Bark"]) - 1))
			Embed = discord.Embed(title = "*WUFF*", description = f"{context.message.author.mention} wants a treat.", colour = discord.Colour.random(seed = time.time()))
			Embed.set_image(url = str(self.urls["Bark"][selection]))
			await context.send(embed = Embed)
			

# ------------------------------------------------------------------------------------------------------------------------------------------------------
# Give Pats
# ------------------------------------------------------------------------------------------------------------------------------------------------------

	@commands.command(name = "Givepats", aliases = ["Givepat", "Patnow", "Givemepats"])
	async def Givepats(self, context : commands.Context):
		selection = random.randint(0, (len(self.urls["Give_Pats"]) - 1))
		Embed = discord.Embed(title = "*Give me pats*", description = f"{context.message.author.mention} wants pats, NOW!.", colour = discord.Colour.random(seed = time.time()))
		Embed.set_image(url = str(self.urls["Give_Pats"][selection]))
		await context.send(embed = Embed)

# ------------------------------------------------------------------------------------------------------------------------------------------------------
# Bonks
# ------------------------------------------------------------------------------------------------------------------------------------------------------

	@commands.command(name = "Bonk", aliases = ["Bonks", "givebonks"])
	async def Bonk(self, context : commands.Context, reciever : str = None):
		if reciever is not None:
			if reciever.find("&") == -1:
				selection = random.randint(0, (len(self.urls["Bonks"]) - 1))
				Embed = discord.Embed(title = "*Bonk*", description = f"{context.message.author.mention} bonks {reciever}.", colour = discord.Colour.random(seed = time.time()))
				Embed.set_image(url = str(self.urls["Bonks"][selection]))
				await context.send(embed = Embed)
			else:
				selection = random.randint(0, (len(self.urls["Bonks"]) - 1))
				Embed = discord.Embed(title = "*Bonk*", description = f"{context.message.author.mention} bonks everyone in {reciever}.", colour = discord.Colour.random(seed = time.time()))
				Embed.set_image(url = str(self.urls["Bonks"][selection]))
				await context.send(embed = Embed)
		else:
			selection = random.randint(0, (len(self.urls["Bonks"]) - 1))
			Embed = discord.Embed(title = "*Bonk*", description = f"{context.message.author.mention} bonks {context.message.author.mention}.", colour = discord.Colour.random(seed = time.time()))
			Embed.set_image(url = str(self.urls["Bonks"][selection]))
			await context.send(embed = Embed)

# ------------------------------------------------------------------------------------------------------------------------------------------------------
# Horny Bonk
# ------------------------------------------------------------------------------------------------------------------------------------------------------

	@commands.command(name = "Horny", aliases = ["Hornybonk", "Hornyjail"])
	async def HBonk(self, context : commands.Context, reciever : str = None):
		if reciever is not None:
			if reciever.find("&") == -1:
				selection = random.randint(0, 3)
				Embed = discord.Embed(title = "*Go to horny jail.*", description = f"{context.message.author.mention} sends {reciever} to horny jail.", colour = discord.Colour.random(seed = time.time()))
				Embed.set_image(url = str(self.urls["Horny_Bonks"][selection]))
				await context.send(embed = Embed)
			else:
				selection = random.randint(0, 3)
				Embed = discord.Embed(title = "*Go to horny jail.*", description = f"{context.message.author.mention} sends everyone in {reciever} to horny jail.", colour = discord.Colour.random(seed = time.time()))
				Embed.set_image(url = str(self.urls["Horny_Bonks"][selection]))
				await context.send(embed = Embed)
		else:
			Embed = discord.Embed(title = "*Go to horny jail.*", description = f"{context.message.author.mention} sends themselves to horny jail.", colour = discord.Colour.random(seed = time.time()))
			Embed.set_image(url = str(self.urls["Horny_Bonks"][4]))
			await context.send(embed = Embed)

# ------------------------------------------------------------------------------------------------------------------------------------------------------
# Tailwag
# ------------------------------------------------------------------------------------------------------------------------------------------------------

	@commands.command(name = "tailwag", aliases = ["wag", "wags", "wagging", "tailwags"])
	async def Tailwag(self, context : commands.Context):
		selection = random.randint(0, 6)
		Embed = discord.Embed(title = "*Wags tail*", description = f"{context.message.author.mention} wags their tail.", colour = discord.Colour.random(seed = time.time()))
		Embed.set_image(url = str(self.urls["Tail_Wag"][selection]))
		await context.send(embed = Embed)

# ------------------------------------------------------------------------------------------------------------------------------------------------------
# Boop
# ------------------------------------------------------------------------------------------------------------------------------------------------------
	
	@commands.command(name = "Boop", aliases = ["Boops", "Boopers"])
	async def Boop(self, context : commands.Context, reciever : str = None):
		if reciever is not None:
			if reciever.find("&") == -1:
				selection = random.randint(0, len(self.urls["Boops"]) - 1)
				Embed = discord.Embed(title = "*Boop*", description = f"{context.message.author.mention} boops {reciever}.", colour = discord.Colour.random(seed = time.time()))
				Embed.set_image(url = str(self.urls["Boops"][selection]))
				await context.send(embed = Embed)
			else:
				selection = random.randint(0, len(self.urls["Boops"]) - 1)
				Embed = discord.Embed(title = "*Boop*", description = f"{context.message.author.mention} boops everyone in {reciever}.", colour = discord.Colour.random(seed = time.time()))
				Embed.set_image(url = str(self.urls["Boops"][selection]))
				await context.send(embed = Embed)
		else:
			selection = random.randint(0, len(self.urls["Boops"]) - 1)
			Embed = discord.Embed(title = "*Boop*", description = f"{context.message.author.mention} boops themselves.", colour = discord.Colour.random(seed = time.time()))
			Embed.set_image(url = str(self.urls["Boops"][selection]))
			await context.send(embed = Embed)

# ------------------------------------------------------------------------------------------------------------------------------------------------------
# END
# ------------------------------------------------------------------------------------------------------------------------------------------------------