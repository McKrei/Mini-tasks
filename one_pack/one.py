'''
Вывести числа от 1 до 100 если кратно 3-м 'Fizz' если 5-ти 'Buzz'. Если то и другое FizzBuzz
'''

def foo():
    for i in range(1, 101):
        show = ''
        if i % 3 == 0: show += 'Fizz'
        if i % 5 == 0: show += 'Buzz'
        print(show if show else i)

foo()


