import unittest
import numpy as np
import os
from core.decode import dimacs2var, var2board

class TestCore(unittest.TestCase):
	
	def setUp(self):
		self.sudoku_array_solved = np.array([
			[5, 3, 4, 6, 7, 8, 9, 1, 2],
			[6, 7, 2, 1, 9, 5, 3, 4, 8],
			[1, 9, 8, 3, 4, 2, 5, 6, 7],
			[8, 5, 9, 7, 6, 1, 4, 2, 3],
			[4, 2, 6, 8, 5, 3, 7, 9, 1],
			[7, 1, 3, 9, 2, 4, 8, 5, 6],
			[9, 6, 1, 5, 3, 7, 2, 8, 4],
			[2, 8, 7, 4, 1, 9, 6, 3, 5],
			[3, 4, 5, 2, 8, 6, 1, 7, 9]
		], dtype=np.int16)

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

	def test_var2board(self):
		with open(self.input_path, 'r') as f:
			dimacs = f.read()
		vars = dimacs2var(dimacs)
		board = var2board(vars)
		self.assertTrue(np.all(board == self.sudoku_array_solved))
