import sys
from core.decode import dimacs2var, var2board
from utils.sudoku_io import write_sudoku, print_sudoku, print_time, extract_time

def main():
	# read DIMACS
	dimacs = sys.stdin.read()
	# convert to variables
	vars = dimacs2var(dimacs)
	# convert to board
	board = var2board(vars)
	print_sudoku(board)
	print_time(extract_time(dimacs), msg='Time to solve')
	# write to file
	write_sudoku(sys.stdout, board)

if __name__ == '__main__':
	main()
