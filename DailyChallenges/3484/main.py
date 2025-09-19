class Spreadsheet:

    def __init__(self, rows: int):
        self.rows = rows
        self.data = {}

    def setCell(self, cell: str, value: int) -> None:
       self.data[cell] = value

    def resetCell(self, cell: str) -> None:
        if cell in self.data:
            del self.data[cell]

    def getValue(self, formula: str) -> int:
        expr = formula[1:]
        left, right = expr.split('+')
        def get_value(token):
            if token.isdigit():
                return int(token)
            else:
                return self.data.get(token, 0)
        val_left = get_value(left)
        val_right = get_value(right)
        return val_left + val_right
# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)
