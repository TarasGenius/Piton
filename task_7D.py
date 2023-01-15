
def deco(*s):
    def decorator(funk):
        def wrapper(*args):
            dct = {}
            lst = []
            n = 0
            integ = 0
            strin = 0
            for i in s:
                if type(i) == str:
                    n += 1
                    strin += 1
                    dct[i] = 'str'
                elif type(i) == int:
                    n += 1
                    integ += 1
                    dct[i] = 'int'
            lst.append(integ)
            lst.append(strin)
            dct[n] = lst
            funk(dct.items())
        return wrapper
    return decorator



@deco(1, 2, 3, '5', 'asd')
def main(*args):
    print('main', args)

main()
