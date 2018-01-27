import unittest
from .. import transaction

class TestTransactionMethods(unittest.TestCase):
	def test_constructor(self):
		t = Transaction()
		self.assertEqual("1", "1")
		# with self.assertRaises(Exception):
		# 	my_graph.compute_distance("dffg12")