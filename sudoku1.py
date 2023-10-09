import sys, time
from core.encode import board2cnf, cnf2dimacs
from utils.sudoku_io import read_sudoku, print_sudoku, print_time

def main():
	# read sudoku
	sudoku_array = read_sudoku(sys.stdin)
	print_sudoku(sudoku_array)
	# convert to CNF
	start_time = time.time()
	cnf = board2cnf(sudoku_array)
	end_time = time.time()
	print_time(end_time - start_time, msg='Time to build CNF')
	# convert to DIMACS
	dimacs = cnf2dimacs(cnf)
	# write to file
	sys.stdout.write(dimacs)

if __name__ == '__main__':
	main()
