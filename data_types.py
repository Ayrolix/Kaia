import json

from dataclasses import dataclass

@dataclass
class User:
	username: str
	wallet: int
	bank: int

@dataclass
class Item:
	name: str
	rarity: str
	quantity: int
	price: int

class Database:
	def __init__(self, filename):
		self.filename = filename
		self.cache_list = []
		with open(filename, "r") as f:
			self.data = json.load(f)

	def commit_data(self):
		with open(self.filename, "w") as f:
			json.dump(self.data, f, indent = 4)

	def pull_user(self, username):
		if username not in self.data:
			self.data[username] = {"wallet": 0, "bank": 5000}
		return User(username, self.data[username]["wallet"], self.data[username]["bank"])

	def commit_user(self, user: User):
		self.data[user.username]["wallet"] = user.wallet
		self.data[user.username]["bank"] = user.bank