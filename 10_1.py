class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                print(f'{self.matrix[i][j]}\t', end='')
            print('')
        return ''

    def __add__(self, other):
        for i in range(len(self.matrix)):
            for j in range(len(other.matrix[i])):
                self.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return Matrix.__str__(self)


a = Matrix([[1, 2, 3], [5, 6, 7], [8, 9, 10]])
b = Matrix([[3, 2, 1], [7, 6, 5], [10, 9, 8]])

print(a)
print(b)
print(a + b)
