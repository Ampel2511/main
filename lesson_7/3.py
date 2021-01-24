class Cell:

    def __init__(self, cells):
        self.cells = cells

    def __add__(self, other):
        return f"{self.cells + other.cells}"

    def __sub__(self, other):
        if self.cells > other.cells:
            return f"{self.cells - other.cells}"
        else:
            return "Клеток в 1м экземпляре должно быть больше, чем во 2м"

    def __mul__(self, other):
        return f"{self.cells * other.cells}"

    def __truediv__(self, other):
        return f"{self.cells // other.cells}"

    def make_order(self, param):
        all_cells = "*" * self.cells
        print("\n".join([all_cells[x:x + param] for x in range(0, len(all_cells), param)]))


cell_8 = Cell(8)
cell_3 = Cell(3)
cell_25 = Cell(25)

print(cell_8 + cell_3)
print(cell_8 - cell_3)
print(cell_8 * cell_3)
print(cell_8 / cell_3)
print(cell_8 - cell_25)

cell_25.make_order(7)
