# Sudoku SAT Solver
A program that parses a sudoku into CNF clauses encoded in DIMACS format, uses the CaDiCaL SAT solver to solve them and transforms the result to a sudoku again with the solution.

## Requirements
### Windows
- Git
- Python (tested on `3.9`) with `numpy`
- A C++ compiler (like g++)
- WSL (Windows Subsystem for Linux)
### Linux
- Git
- Python (tested on `3.9`) with `numpy`
- A C++ compiler (like g++)

## Usage
Clone this repo (recursively so that the cadical submodule is also downloaded):
`git clone --recurse-submodules https://github.com/Pikurrot/sudoku-sat-solver.git`

### Windows
1. Run `run_solver.bat`
2. Enter the name of the sudoku file (eg. `ex_0000`) without extension. Input sudokus must be placed inside `input/` folder.

The solved sudoku will appear as a .suk file in `/output` with the same name as the input file prefixed with "sol_" (eg. `sol_ex_0000.suk`). The CNF formulas will be saved in `/dimacs`, as well as the SAT solver result.

Alternatively, you can do it manually, from WSL, following the same steps as in [Linux](#linux-1).
### Linux
```
cd cadical
./configure && make
cd ..
python sudoku1.py < "input/ex_0000.suk" > "dimacs/ex_0000.cnf"
./cadical/build/cadical "dimacs/ex_0000.cnf" > "dimacs/ex_0000.out"
python sudoku2.py < "dimacs/ex_0000.out" > "output/sol_ex_0000"
```
**Note**: `./configure && make` is only necessary to run once, when you clone this repo.

## Considerations
The input sudoku must be in a `.suk` file, which is simply a plain text file that you can create as `.txt` file and rename it. `.cnf` and `.out` files can also be visualized as plain text. With the manual approach, you should also be able to pass `.txt` files to the programs.

Example files of each type have been provided at [input](input), [dimacs](dimacs) and [output](output) folders.

The [core/](core) folder contains the core functions used in [sudoku1.py](sudoku1.py) and [sudoku2.py](sudoku2.py), along with a [README](core/README.md) explaining the `board2cnf()` function, which is the responsible to generate the CNF clauses from the sudoku initial state.

## Acknowledgments
- CaDiCaL SAT solver: https://github.com/arminbiere/cadical
