

class First:
    def __init__(self, a):
        self.a = a
        print(self.a)
    def method(self, *args):
        self.keys = set(map(tuple, args))
        print(self.keys)
        print(type(self.keys), len(self.keys))

class Second(First):
    def __init__(self, b, c, a):
        super().__init__(a)
        self.b = b
        self.c = c
        print(self.b, self.c)


    def method(self, **kwargs):
        super().method(set(map(str, kwargs.keys())))
        self.values = set(map(str, kwargs.values()))
        print(self.values)
        print(type(self.values))




obj = Second(1, 2, 3)
objj= obj.method(name='Tom', age='12')





