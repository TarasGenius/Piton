
class First:
    def __init__(self, a):
        self.a = a

    def method(self):
        return self.__dict__

    def method_two(self):
        return self.__dict__


class Second:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def method(self):
        return self.__dict__

    def method_two(self):
        return self.__dict__


class Third:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def method(self):
        return self.__dict__


class Fourth:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def nomethod(self):
        return self.__dict__


obj_f = First(1)
obj_s = Second(1, 2)
obj_t = Third(1, 2, 3)
obj_ch = Fourth(1, 2, 3, 4)

lst_obj = [obj_f, obj_s, obj_t, obj_ch]


def task_one():
    lst_met = []
    for i in lst_obj:
        try:
            i.method()
        except AttributeError:
            lst_obj.remove(i)
        else:
            lst_met.append(i.method)
    return dict(zip(lst_obj, lst_met))


dct = task_one()
print(f'task one {dct}')


def task_two():
    lst_met = []
    lst_met_for_method_two = []
    lst_obj_for_method_two = lst_obj.copy()
    for i in lst_obj:
        try:
            i.method()
        except AttributeError:
            lst_obj.remove(i)
        else:
            lst_met.append(i.method)

        try:
            i.method_two()
        except AttributeError:
            lst_obj_for_method_two.remove(i)
        else:
            lst_met_for_method_two.append(i.method_two)
    return dict(zip(lst_obj, lst_met)), dict(zip(lst_obj_for_method_two, lst_met_for_method_two))


first_dct, second_dct = task_two()

print(f'Task two, first dct {first_dct}')
print(f'Task two, second dct {second_dct}')
