import unittest
import numpy as np
import os
from utils.sudoku_io import read_sudoku

class TestSudokuIO(unittest.TestCase):
	
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
		self.file_path = os.path.join('tests', 'example.suk')

	def tearDown(self):
		pass

	def test_read_sudoku(self):
		read_array = read_sudoku(self.file_path)
		np.testing.assert_array_equal(read_array, self.sudoku_array)
