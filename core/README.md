# Core package for sudoku-sat-solver
This package contains the core logic and algorithms for the solver.

## Board to CNF algorithm explanation
The following is an explanation of the algorithm used to convert a 9x9 sudoku board to a CNF formula that can then be solved by a SAT solver. I used a `numpy` approach to make it as much efficient as possible, which resulted in a quite abstract algorithm.  
The sudoku can be simply seen as a 2D matrix. To pass it to CNF, each 1x1 cell can have a value in the range [1,9], so we can now represent it as a 3D tensor, where the 3rd dimension represent all 9 possible values each cell can take. As CNF needs variables, not values, this tensor will actually be an ID tensor, where each entry is a unique ID.  
The first statement refers to incorporating the initial state of the board as literal clauses in the CNF:  
- For every cell *(i,j)* with an initial value *k*, add *X<sup>k</sup><sub>ij</sub>*  

This can be achieved by simply taking the non-zero values and adding their corresponding IDs to the list of clauses.  
Now, the following statements will create additional CNF clauses:
1. For every row *i = 0, ..., 8* and every value *k = 0, ..., 8* there is a *k* at row *i*, i.e.: *X<sup>k</sup><sub>i0</sub>* ∨ ... ∨ *X<sup>k</sup><sub>i8</sub>*
2. For every column *j = 0, ..., 8* and value *k = 0, ..., 8* there is a *k* at column *j*, i.e.: *X<sup>k</sup><sub>0j</sub>* ∨ ... ∨ *X<sup>k</sup><sub>8j</sub>*
3. For every *3x3* square there is a value *k = 0, ..., 8*.

The three statements can be achieved by "looking" at the tensor from different perspectives and reshaping it.  
The first statement makes *i* and *k* free variables, while *j* is fixed, so it's like sliding a *1x9x1* vector through the tensor, first through the *k* dimension and then through the *i* dimension. Instead of doing it in 2 loops, the same effect can be achieved by transposing the tensor in the appropiate way and then reshaping it from there to a 2D array, where each row will be a clause of 9 variables (IDs).  
The second statement is the same as the first one, but with columns, so it must be transposed in a different way.  
The same can be done in the third statement, but first, the 9 3x3 squares must be extracted for each possible value. This involves extracting 9 3x3x9 blocks from the tensor and rearranging them into multiple 3x3 squares (kind of slicing each block), and then converting each square into a 1x9 vector, which will be the clause.  
Now, there is a restriction that must be included in the CNF:
- For every cell *(i,j)* and pair of values *k != k'* we cannot have both *k* and *k'* at the same cell: *¬X<sup>k</sup><sub>ij</sub> ∨ ¬X<sup>k'</sup><sub>ij</sub>*

First, all combinations of pairs for a cell are listed, and only those that satisfy *k1 < k2* are taken. This method effectively ensures that *k1 != k2* and no pair is repeated, achieved by applying a mask and taking the indices where the condition is satisfied. These indices are used in the *k* axis of the tensor, extracting the IDs of the pairs of values at those indices. Finally, the pairs are negated and joined to form a clause for each pair.  
By putting together all the clauses from the statements and restriction, it is possible to convert them to DIMACS format and forward them to the SAT solver.