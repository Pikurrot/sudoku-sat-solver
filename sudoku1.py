import sys
from core.encode import board2cnf, cnf2dimacs
from utils.sudoku_io import read_sudoku

def main():
	# read sudoku
	sudoku_array = read_sudoku(sys.stdin)
	# convert to CNF
	cnf = board2cnf(sudoku_array)
	# convert to DIMACS
	dimacs = cnf2dimacs(cnf)
	# write to file
	sys.stdout.write(dimacs)

if __name__ == '__main__':
	main()
