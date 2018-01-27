import user

class Transaction(Object):
	def __init__(self):
		self.payer = None
		self.payee = None
		self.amount = None
		self.signature = None