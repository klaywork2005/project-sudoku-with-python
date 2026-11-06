from typing import Tuple
import clingo


class Sudoku:
    def __init__(self, sudoku: dict[Tuple[int, int], int]):
        self.sudoku = sudoku

    def __str__(self) -> str:
        s = ""
        for row in range(1, 10):
            for column in range(1, 10):
                s = s + str(self.sudoku[(row,column)])
                if column != 3 and column != 6:
                    s = s + " "
                else:
                    s = s + "  "
            s = s + "\n"
            if row == 3 or row == 6:
                s = s + "\n"
        return s

    @classmethod
    def from_str(cls, s: str) -> "Sudoku":
        sudoku = {}
        # YOUR CODE HERE
        return cls(sudoku)

    @classmethod
    def from_model(cls, model: clingo.solving.Model) -> "Sudoku":
        sudoku = {}
        for symbol in model.symbols(shown=True):
            if symbol.name == "sudoku":
                arguments = symbol.arguments
                row = arguments[0].number
                column = arguments[1].number
                numberInSquare = arguments[2].number
                sudoku[(row, column)] = numberInSquare
        return cls(sudoku)
