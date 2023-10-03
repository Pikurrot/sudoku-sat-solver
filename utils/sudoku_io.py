import numpy as np
import os

def read_sudoku(filename: str) -> np.ndarray:
	"""
	Parses a sudoku puzzle from a file into a NumPy array.
	"""
	with open(filename, 'r') as f:
		lines = f.readlines()
	lines = [l.strip() for l in lines]
	puzzle = np.zeros((9, 9), dtype=np.int16)
	for i, line in enumerate(lines):
		for j, char in enumerate(line):
			if char != '.':
				puzzle[i, j] = int(char)
	return puzzle