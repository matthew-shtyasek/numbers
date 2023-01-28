class Comment:
    def __init__(self, authors, text):
        self.authors = authors
        self.text = text

    def __add__(self, other):
        result = Comment(self.authors, self.text)
        result.authors += other.authors
        result.text += other.text
        return result

    

    def __str__(self):
        return f'{self.authors}\n{self.text}'


a = Comment(['Vasya'], "abcdefg")
b = Comment(['Чукча', "BBC"], "абвгдеёжз")
print(a+b)