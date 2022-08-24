'''
Условие:

Создать функцию которая принимает строку и заменяет каждую букву на её позицию в алфавите. Если что-то в тексте не является буквой, игнорируйте это и не возвращайте. На выходе получаем строку.

Пример:
Ф-ция принимает: "I learn Python with Python Nation!!!"

Ф-ция возвращает: "9 12 5 1 18 14 16 25 20 8 15 14 23 9 20 8 16 25 20 8 15 14 14 1 20 9 15 14"
'''

from string import ascii_lowercase
letters_dict = {l: str(i) for l, i in zip(ascii_lowercase, range(1, 27))}

def encoding(string: str) -> str:
    result_list = [letters_dict[l] for l in string if l in ascii_lowercase]
    return ' '.join(result_list)

encoding2 = lambda s: ' '.join([letters_dict[l] for l in s if l in ascii_lowercase])

def alphaNum(s):
    return ' '.join([str(ord(c)-96) for c in s.lower() if c.isalpha()])
