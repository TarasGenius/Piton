
#calculator - first task, ver 1

'''
fnum = float(input('Enter first num: '))
snum = float(input('Enter second num: '))
oper = input('Enter +, -, *, /: ')


add = '+'
sub = "-"
multi = '*'
div = '/'
result = float(0)

if oper == add:
    result = fnum + snum
elif oper == sub:
    result = fnum - snum
elif oper == multi:
    result = fnum * snum
elif oper == div and snum != 0:
    result = fnum * snum
else:
    print('Entered invalid variable or operand')

print(result)

'''
#calculator ver 2

try:
    fnum = float(input('Enter first num: '))
    snum = float(input('Enter second num: '))
    oper = input('Enter +, -, *, /: ')
    lst = ['+', '-', '*', '/']


    dct = {'+': lambda a, b: a+b,
           '-': lambda a, b: a-b,
           '*': lambda a, b: a*b,
           '/': lambda a, b: a/b
       }

    print(dct[oper](fnum, snum))

except ZeroDivisionError:
    print('Division by zero')
except:
    print('invalid')



