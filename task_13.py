
class First:
    def __init__(self, a):
        self.a = a
        print(self.a)

    def method(self, *args):
        self.keys = set(map(tuple, args))
        return self.keys


class Second(First):
    def __init__(self, b, c, a):
        super().__init__(a)
        self.b = b
        self.c = c
        print(self.b, self.c)

    def method(self, **kwargs):
        self.values = set(map(str, kwargs.values()))
        return super().method(set(map(str, kwargs.keys()))), self.values


obj = Second(1, 2, 3)
a, b = obj.method(name='Tom', age='12', less='13')
print(a)
print(b)



