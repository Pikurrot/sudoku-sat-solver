import unittest
import numpy as np
import os
from core.encode import board2cnf

class TestCore(unittest.TestCase):
	
	def setUp(self):
		self.sudoku_array = np.array([
			[5, 3, 0, 0, 7, 0, 0, 0, 0],
			[6, 0, 0, 1, 9, 5, 0, 0, 0],
			[0, 9, 8, 0, 0, 0, 0, 6, 0],
			[8, 0, 0, 0, 6, 0, 0, 0, 3],
			[4, 0, 0, 8, 0, 3, 0, 0, 1],
			[7, 0, 0, 0, 2, 0, 0, 0, 6],
			[0, 6, 0, 0, 0, 0, 2, 8, 0],
			[0, 0, 0, 4, 1, 9, 0, 0, 5],
			[0, 0, 0, 0, 8, 0, 0, 7, 9]
		], dtype=np.int16)

	def tearDown(self):
		pass

	def test_board2cnf(self):
		cnf = board2cnf(self.sudoku_array)
		# lenght is correct
		n_initial = np.count_nonzero(self.sudoku_array)
		self.assertEqual(len(cnf), n_initial + 81*3 + 9*9*36)
		# check first n_initial have length 1
		self.assertTrue(np.all(np.array([len(clause) for clause in cnf[:n_initial]]) == 1))
		# check the next 81*3 have length 9
		self.assertTrue(np.all(np.array([len(clause) for clause in cnf[n_initial:n_initial+81*3]]) == 9))
		# check the last 9*9*36 have length 2
		self.assertTrue(np.all(np.array([len(clause) for clause in cnf[-9*9*36:]]) == 2))
		# check no clause is repeated
		self.assertEqual(len(cnf), len(set([tuple(clause) for clause in cnf])))
