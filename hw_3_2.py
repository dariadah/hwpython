index_numb = int(input('Введите порядковый номер >>> '))
def fibonacci(numb):
    if numb == 1 or numb == 2:
        return 1
    else:
        return fibonacci(numb - 1) + fibonacci(numb - 2)
print(fibonacci(index_numb))
