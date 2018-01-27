import hashlib

class Block(Object):
	def __init__(self, author, transactions, previous_block_hash):
		""" initializes a block """
		self.transactions = transactions
		self.proof_of_work = None
		self.previous_block_hash = previous_block_hash
		self.next_block = None
		self.reward_transaction = None
		self.author = author

	def get_hash(self):
		m = str(self.transactions) + str(self.previous_block_hash)
		sha256 = hashlib.sha256()
		return sha256.update(m).hexdigest()

	def __repr__(self):
		pass

	def __str__(self):
		pass