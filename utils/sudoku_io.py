import numpy as np
import os, sys, re
from typing import Union, TextIO

def read_sudoku(file_input: Union[str, TextIO]) -> np.ndarray:
	"""
	Parses a sudoku from a file into a NumPy array.
	"""
	if isinstance(file_input, str):
		with open(file_input, 'r') as f:
			lines = f.readlines()
	else:
		lines = file_input.readlines()
	
	lines = [l.strip() for l in lines]
	board = np.zeros((9, 9), dtype=np.int16)
	for i, line in enumerate(lines):
		for j, char in enumerate(line):
			if char != '.':
				board[i, j] = int(char)
	return board

def write_sudoku(file_output: Union[str, TextIO], board: np.ndarray) -> None:
	"""
	Writes a sudoku from a NumPy array into a file.
	"""
	if isinstance(file_output, str):
		with open(file_output, 'w') as f:
			for i in range(9):
				for j in range(9):
					f.write(str(board[i, j]))
				f.write('\n')
	else:
		for i in range(9):
			for j in range(9):
				file_output.write(str(board[i, j]))
			file_output.write('\n')

def print_sudoku(board: np.ndarray) -> None:
	"""
	Prints a sudoku from a NumPy array.
	"""
	string = '+-------+-------+-------+\n'
	for i in range(9):
		string += '| {} {} {} | {} {} {} | {} {} {} |\n'.format(*board[i])
		if (i + 1) % 3 == 0 and i < 8:
			string += '|-------+-------+-------|\n'
	string += '+-------+-------+-------+\n'
	sys.stderr.write(string)

def print_time(elapsed_time: float, msg: str='Time elapsed') -> None:
	"""
	Prints the time elapsed between start_time and end_time.
	"""
	sys.stderr.write(f'{msg}: {elapsed_time:.3f} s\n')

def extract_time(string: str):
	"""
	Extracts the time taken from a string in DIMACS format.
	"""
	time_pattern = re.compile(r'c total process time since initialization:\s*([\d.]+)\s*seconds')

	for line in string.splitlines():
		match = time_pattern.search(line)
		if match:
			return float(match.group(1))
	return None
