"""Всё, что начинается с двух нижних
подчёркиваний - магические методы"""


class Matrix:
    def __init__(self, w, h):  # конструктор класса
        self.matrix = [[0 for i in range(w)] for i in range(h)]

    def __str__(self):  # преобразование объекта в строку
        result = ""
        for line in self.matrix:
            for item in line:
                result += str(item)
            result += '\n'
        return result

    def __getitem__(self, item):  # магический метод для перегрузки индексирования
        # позволяет обращаться к классу как к массиву
        return self.matrix[item]

    def __add__(self, other):  # сложение
        # чтобы сложить класс с классом нужно задать правила их сложения
        if not isinstance(other, Matrix):
            raise TypeError('Второй операнд тоже должен быть матрицей')
        if len(self.matrix[0]) != len(other.matrix[0]) or len(self.matrix) != len(other.matrix):
            raise ArithmeticError('Матрицы не совпадают по размерности')

        result = Matrix(len(self.matrix[0]), len(self.matrix))
        for self_line, other_line, y in zip(self.matrix, other.matrix, range(len(self.matrix))):
            for self_item, other_item, x in zip(self_line, other_line, range(len(self_line))):
                result[y][x] = self_item + other_item
        return result


m = Matrix(4, 3)
n = Matrix(4, 3)
print(m)
print(m[0])
m[0][1] = 1
n[0][1] = -1
n[1][0] = 9
print(m)
print(m + n)

for i,j in zip([1, 2, 3], [4, 5, 6]):
    print(i, j)
