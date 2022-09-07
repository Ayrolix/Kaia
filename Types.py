import json

from dataclasses import dataclass

class User:
	def __init__(self, username, wallet, bank) -> None:
		self.username = username
		self.wallet = wallet
		self.bank = bank

class Record:
	def __init__(self, path) -> None:
		self.path = path
		self.cache = []
		with open(self.path, "r") as f:
			self.records = json.load(f)
	
	#function to save self.records to the self.path file
	def save(self):
		with open(self.path, "w") as f:
			json.dump(self.records, f, indent = 4)
	
	#function to add a record to self.records
	def get_user(self, username):
		if username not in self.records:
			self.records[username] = { "wallet": 0, "bank": 0 }
			self.save()
		return User(self.records[username], self.records[username]["wallet"], self.records[username]["bank"])

	def set_user(self, user):
		self.data[user.username]["wallet"] = user.wallet
		self.data[user.username]["bank"] = user.bank