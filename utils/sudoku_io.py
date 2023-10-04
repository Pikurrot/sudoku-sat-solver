import numpy as np
import os

def read_sudoku(file_path: str) -> np.ndarray:
	"""
	Parses a sudoku from a file into a NumPy array.
	"""
	with open(file_path, 'r') as f:
		lines = f.readlines()
	lines = [l.strip() for l in lines]
	board = np.zeros((9, 9), dtype=np.int16)
	for i, line in enumerate(lines):
		for j, char in enumerate(line):
			if char != '.':
				board[i, j] = int(char)
	return board

def write_sudoku(file_path: str, board: np.ndarray) -> None:
	"""
	Writes a sudoku from a NumPy array into a file.
	"""
	with open(file_path, 'w') as f:
		for row in board:
			for num in row:
				if num == 0: f.write('.')
				else: f.write(str(num))
			f.write('\n')