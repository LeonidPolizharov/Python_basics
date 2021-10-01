class Cell:
    def __init__(self, cells):
        self.cells = int(cells)

    def __add__(self, other):
        return Cell(self.cells + other.cells)

    def __sub__(self, other):
        if self.cells - other.cells < 0:
            print("Кол-во клеток меньше нуля")
            exit(0)
        else:
            return Cell(self.cells - other.cells)

    def __mul__(self, other):
        self.cells = self.cells * other.cells
        return self.cells

    def __floordiv__(self, other):
        return Cell(self.cells * other.cells)

    def make_order(self, row):
        block = self.cells // row
        last_block = self.cells % row
        for i in range(block):
            print('*' * row, end='\n')
        print('*' * last_block)


a = Cell(3)
# print(a.cells)
b = Cell(12)

b.make_order(5)


print(b - a - b)
