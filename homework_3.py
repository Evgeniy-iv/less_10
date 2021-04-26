class Cell:
    def __init__(self, number_of_cells):
        self.number_of_cells = number_of_cells

    def __add__(self, other):
        return Cell(self.number_of_cells + other.number_of_cells)

    def __sub__(self, other):
        result = self.number_of_cells - other.number_of_cells
        if result > 0:
            return Cell(result)
        else:
            return 'Количество клеток не может быть отрицательным'

    def __mul__(self, other):
        return Cell(self.number_of_cells * other.number_of_cells)

    def __floordiv__(self, other):
        return Cell(self.number_of_cells // other.number_of_cells)

    def __str__(self):
        return f'{self.number_of_cells}'

    def make_order(self, number_of_cells_in_a_row):
        cells_string = '*' * self.number_of_cells
        strings_list = [cells_string[i:i + number_of_cells_in_a_row] for i in
                        range(0, len(cells_string), number_of_cells_in_a_row)]
        string = '\n'.join(strings_list)
        return string


if __name__ == '__main__':
    cell_1 = Cell(24)
    cell_2 = Cell(5)
    cell_add = cell_1 + cell_2
    cell_sub = cell_1 - cell_2
    cell_mul = cell_1 * cell_2
    cell_div = cell_1 // cell_2
    print(cell_add, cell_sub, cell_mul, cell_div)
    print(cell_add.make_order(5))
    print(cell_sub.make_order(4))
    print(cell_mul.make_order(6))
    print(cell_div.make_order(7))

