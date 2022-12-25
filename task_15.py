
# task 1

class Main:
    def __init__(self, a):
        self.a = a

    @staticmethod
    def stat(*args):
        for i in args:
            if isinstance(i, str):
                if i.isdigit() == False:
                    return i
            else:
                raise TypeError


obj = Main(Main.stat('1', 'qwe', 4))

print(obj.__dict__)


# task 2

dct_main = {(1,): ['tom', 25],
            (2,): ['ana', 30],
            'jaja': ['lisa', 15],
            'plan': ['greta', 50]
}


class MainTaskTwo:
    def __init__(self, lst):
        self.name = lst[0]
        self.age = lst[1]

    @classmethod
    def clas(cls, dct):
        lst = []
        for i in dct:
            if isinstance(i, str):
                globals()[i] = cls(dct[i])
                lst.append(i)
        return lst


g = MainTaskTwo.clas(dct_main)

print(g)
for i in g:
    print(f' name obj: {i}\n atributs {globals()[i].__dict__}')
