class Number:
    def __init__(self, number, sign):
        self.number = number
        self.sign = sign

    def __add__(self, other):
        result = Number(0, '')
        if self.sign != other.sign:
            if self.sign == '-':
                if self.number > other.number:
                    result.sign = '-'
            else:
                if other.number > self.number:
                    result.sign = '-'
            if result.sign == '':
                result.sign = '+'
            result.number = abs(self.number - other.number)
        else:
            result.number = (self.number + other.number)
            result.sign = self.sign
        if result.number == 0:
            result.sign = ''
        return result

    def __str__(self):
        return self.sign + str(self.number)

a = Number(4, '+')
b = Number(5, '-')
print(a + b)

