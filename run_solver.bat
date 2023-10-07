@echo off

:: User input file name
set /p FileName="Enter the name of the .suk file (without extension): "

:: Run the solver
python sudoku1.py < input\%FileName%.suk > dimacs\%FileName%.cnf

:: Check for errors
if %ERRORLEVEL% neq 0 (
    echo An error occurred while running sudoku1.py
    exit /b %ERRORLEVEL%
) else (
	echo CNF built successfully and saved in dimacs\%FileName%.cnf
)

pause
