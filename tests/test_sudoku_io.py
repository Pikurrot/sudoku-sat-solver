import unittest
import numpy as np
import os
from utils.sudoku_io import read_sudoku, write_sudoku

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
		self.input_path = os.path.join('tests', 'test_data', 'example.suk')
		self.output_path = os.path.join('tests', 'test_data', 'example_out.suk')

	def tearDown(self):
		if os.path.exists(self.output_path):
			os.remove(self.output_path)

	def test_read_sudoku(self):
		read_array = read_sudoku(self.input_path)
		np.testing.assert_array_equal(read_array, self.sudoku_array)

	def test_write_sudoku(self):
		write_sudoku(self.output_path, self.sudoku_array)
		read_array = read_sudoku(self.output_path)
		np.testing.assert_array_equal(read_array, self.sudoku_array)
		
