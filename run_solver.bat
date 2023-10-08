@echo off

:: User input file name
set /p FileName="Enter the name of the .suk file (without extension): "

:: Run sudoku1.py
echo Building CNF for input\%FileName%.suk
python sudoku1.py < "input\%FileName%.suk" > "dimacs\%FileName%.cnf"

:: Check for errors
if %ERRORLEVEL% neq 0 (
	echo An error occurred while running sudoku1.py
	goto :End
) else (
	echo CNF built successfully and saved in dimacs\%FileName%.cnf
)

:: Run cadical via shell script in WSL
wsl chmod +x run_cadical.sh && wsl ./run_cadical.sh "%FileName%"

:: Check for errors
if %ERRORLEVEL% equ 1 (
    echo Could not solve sudoku.
	goto :End
) else if %ERRORLEVEL% equ 10 (
    echo The formula is SATISFIABLE. Solution generated successfully and saved in dimacs/%FileName%.out
) else if %ERRORLEVEL% equ 20 (
    echo The formula is UNSATISFIABLE. See the output in dimacs/%FileName%.out
) else (
    echo An error occurred while running ./cadical/build/cadical.
	goto :End
)

:: Run sudoku2.py
echo Building sudoku board from dimacs\%FileName%.out
python sudoku2.py < "dimacs\%FileName%.out" > "output\%FileName%.suk"

:: Check for errors
if %ERRORLEVEL% neq 0 (
	echo An error occurred while running sudoku2.py
	goto :End
) else (
	echo Sudoku board built successfully and saved in output\%FileName%.suk
)

:End
pause
