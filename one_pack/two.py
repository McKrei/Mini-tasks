'''
Дан отрезок АБ и список случайных отрезков найти кол-во числе которые не пересекаются с АБ в других отрезках
'''


def foo2(a, b, n_list):
    result_numbers = set(range(a, b + 1))
    for A, B in n_list:
        numbers = set(range(A, B + 1))
        result_numbers = result_numbers - numbers
    return len(result_numbers)


a = 15
b = 165
N = [
    [37, 68],
    [52, 74],
    [118, 146],
    [35, 44],
    [37, 65],
    [46, 74]
]
print(foo2(a, b, N))
