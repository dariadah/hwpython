def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a,b):
    return a/b

operations_dict = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': div,
}

def checking():
    while True:
        try:
            main()
        except KeyError as e:
            print('Key Error is here, change characters that you put')
        except ZeroDivisionError as e:
            print('ZeroDivisionError is here, change characters that you put')
        except ValueError as e:
            print('Value Error is here, change characters that you put')
        # except TypeError as e:
        #     print('Type Error is here')
        except ArithmeticError as e:
            print('Arithmetic Error is here, change characters that you put')
        except Exception as e:
            print(type(e))
        # else:
        #     print('Everything is ok')
        #     break

def main():
    first_number = float(input('Put your first number >>> '))
    operation = input('Operation you can do: +|-|*|/ >>> ').strip()
    second_number = float(input('Put your second number >>> '))
    res = None
    if operation in operations_dict.keys():
        res  = operations_dict[operation](first_number , second_number)
    if res is not None:
        print('Result is {} from {}'. format(res, operation))

checking()
main()



