import numpy as np

def dimacs2var(dimacs: str) -> np.ndarray:
	"""
	Extracts the variables from a string in DIMACS format.
	"""
	vars = np.array([], dtype=np.int16)
	for line in dimacs.split('\n'):
		if not line.startswith('v '):
			continue
		literals = line[2:].split()
		for literal in literals:
			if literal == '0':
				break
			vars = np.append(vars, int(literal))
	return vars

def var2board(vars: np.ndarray) -> np.ndarray:
	"""
	Converts an array of variables to a sudoku board.
	"""
	var_tensor = vars.reshape((9, 9, 9)) # put variables back to a tensor
	board = np.argmax(var_tensor, axis=2) + 1 # get the index of the only positive value in each cell
	return board
