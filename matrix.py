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


m = Matrix(4, 3)
print(m)
