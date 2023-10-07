import numpy as np

def board2cnf(board: np.ndarray) -> list:
	"""
	Converts a sudoku board to a list of CNF clauses.
	"""
	id_tensor = np.arange(1, 9*9*9+1, dtype=np.int16).reshape((9, 9, 9)) # assign each entry in tensor a unique id in the range [1, 729]

	# for every cell (i,j) with an initial value k, add k as a literal clause
	i, j = np.nonzero(board) # indices of non-zero elements
	k = board[i, j] - 1 # values of non-zero elements
	cnf0 = id_tensor[i, j, k].reshape(-1, 1) # shape=(N, 1)

	# for every row i and every value k, there is a k in row i
	cnf1 = id_tensor.transpose((0,2,1)).reshape((9*9, 9))
	# for every column j and every value k, there is a k in column j
	cnf1 = np.concatenate((cnf1, id_tensor.transpose((1,2,0)).reshape((9*9, 9))), axis=0)
	# for every 3x3 square and every value k, there is a k in the square
	blocks = id_tensor.reshape(3, 3, 3, 3, 9) # 3x3 grid of 3x3x9 blocks
	grid = blocks.transpose(0, 4, 2, 1, 3) # rearrange to a 3x3 grid of 3x3 squares for each possible value k
	clauses = grid.reshape(9*9, 9) # now each 3x3 square is a clause of shape 1x9
	cnf1 = np.concatenate((cnf1, clauses), axis=0)
			
	# for every cell (i,j) and every pair of values k1 != k2, we can't have both k1 and k2 in (i,j)
	k1, k2 = np.indices((9, 9)) # combination of all pairs of values (values from 0 to 8, as k values in id_tensor range from 0 to 8, but represent 1 to 9). | Both shape=(9,9)
	mask = k1 < k2 # effective way of getting all pairs of values so that k1 != k2 and no pair is repeated. | shape=(9,9)
	i_k1, i_k2 = np.where(mask) # indices of the pairs satisfying k1 < k2. | Both shape=(N,)
	k1, k2 = -np.take(id_tensor, i_k1, axis=2), -np.take(id_tensor, i_k2, axis=2) # take and negate the ids of the pairs of values. | Both shape=(9,9,N)
	cnf2 = np.stack((k1, k2), axis=-1).reshape(-1, 2) # stack the pairs of values together . | shape=(9, 9, N, 2) -> (9*9*N, 2)

	return cnf0.tolist() + cnf1.tolist() + cnf2.tolist()

def cnf2dimacs(cnf: list) -> None:
	"""
	Converts a list of CNF clauses to a string in DIMACS format.
	"""
	n_clauses = len(cnf)
	n_variables = max([max(clause) for clause in cnf])
	header = f'p cnf {n_variables} {n_clauses}\n'
	clauses = '\n'.join([' '.join([str(literal) for literal in clause]) + ' 0' for clause in cnf])
	return header + clauses