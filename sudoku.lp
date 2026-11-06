
{ sudoku(ROW,COL,NUM) : NUM = 1..9 } = 1 :- ROW = 1..9, COL = 1..9.

subgrid(ROW,COL,G) :- ROW = 1..9, COL = 1..9, G = 1+(((ROW-1)/3) *3 +((COL-1))/3).

:- sudoku(ROW1,COL1,NUM), sudoku(ROW2,COL2,NUM), subgrid(ROW1,COL1,G), subgrid(ROW2,COL2,G), (ROW1,COL1) != (ROW2,COL2).

:- initial(ROW,COL,NUM), not sudoku(ROW,COL,NUM).

:- sudoku(ROW1,COL,NUM), sudoku(ROW2,COL,NUM), ROW1 != ROW2.

:- sudoku(ROW,COL1,NUM), sudoku(ROW,COL2,NUM), COL1 != COL2.


#show sudoku/3.