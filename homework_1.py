class Matrix:

    def __init__(self, matr):
        self.matr = matr

    def __str__(self):
        import re
        string = '\n'.join([str(i) for i in self.matr])
        matr_string = re.sub("[^0-9 '\n']", "", string)
        return matr_string

    def __add__(self, other):
        import numpy as p
        ar1 = p.matrix(self.matr)
        ar2 = p.matrix(other.matr)
        res = p.matrix(p.zeros((3, 3)))
        res = ar1 + ar2
        return Matrix(res)


if __name__ == '__main__':
    mc_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    mc_2 = Matrix([[10, 11, 12], [13, 14, 15], [16, 17, 18]])

    print(f'\n{mc_1}')
    print(f'\n{mc_2}')

    print(f'\n{mc_1 + mc_2}')
