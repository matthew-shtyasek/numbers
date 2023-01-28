import copy


class Comment:
    def __init__(self, authors, text):
        self.authors = authors
        self.text = text

    def __add__(self, other):
        result = Comment(copy.copy(self.authors), self.text)
        result += other
        return result

    def __iadd__(self, other):  # +=
        self.authors += other.authors
        self.text += other.text
        return self

    def __str__(self):
        return f'{self.authors}\n{self.text}'


a = Comment(['Vasya'], "abcdefg")
b = Comment(['Чукча', "BBC"], "абвгдеёжз")
print(a + b)
print(a)
a += b
print(a)

a1 = [['Vasya'], "abcdefg"]
b1 = [['Чукча', "BBC"], "абвгдеёжз"]

a1 += b1

print(a1)