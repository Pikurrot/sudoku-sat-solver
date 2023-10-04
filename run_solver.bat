@echo off

:: User input file name
set /p FileName="Enter the name of the .suk file (without extension): "

:: Run the solver
python sudoku1.py < input\%FileName%.suk > output\%FileName%.cnf

pause
