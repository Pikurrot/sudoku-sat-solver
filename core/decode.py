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
