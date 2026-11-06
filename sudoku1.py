import sys, clingo

class ClingoApp(clingo.application.Application):
    def main(self, ctl, files):
        ctl.load("sudoku.lp")
        for f in files:
          ctl.load(f)
        if not files:
            ctl.load("-")
        ctl.ground()
        ctl.solve()

    def print_model(self, model, printer) -> None:
        symbols = model.symbols(shown=True)
        symbols = sorted(symbols)
        print(" ".join(str(s) for s in symbols))
        
clingo.application.clingo_main(ClingoApp())