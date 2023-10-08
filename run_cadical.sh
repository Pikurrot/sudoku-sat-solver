#!/bin/bash

cd cadical

# Check if cadical is built, if not, build it
if [ ! -f "build/cadical" ]; then
	echo Building cadical. This will be a one-time operation.
	./configure && make
	if [ $? -not 0 ]; then
		echo An error occurred while building cadical.
		exit 1
	else
		echo Cadical built
	fi
fi

cd ..

# Run cadical 
echo Running SAT solver with formulas in dimacs/$1.cnf
./cadical/build/cadical "dimacs/$1.cnf" > "dimacs/$1.out"

exit $?
