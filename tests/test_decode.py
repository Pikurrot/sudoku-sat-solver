import unittest
import numpy as np
import os
from core.decode import dimacs2var

class TestCore(unittest.TestCase):
	
	def setUp(self):
		self.input_path = os.path.join('tests', 'test_data', 'example.out')

	def tearDown(self):
		pass

	def test_dimacs2var(self):
		with open(self.input_path, 'r') as f:
			dimacs = f.read()
		vars = dimacs2var(dimacs)
		# check lenght is correct
		self.assertEqual(len(vars), 9*9*9)
		# check vars are not repeated
		self.assertEqual(len(vars), len(np.unique(np.abs(vars))))
		# check vars are in the correct range
		self.assertTrue(np.all(np.abs(vars) <= 9*9*9))
		# check there are no 0
		self.assertFalse(np.any(vars == 0))