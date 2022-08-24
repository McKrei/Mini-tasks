'''
Была введена новая системная политика, которая требует,
чтобы все учетные записи использовали кодовую фразу вместо простого пароля.
Парольная фраза состоит из набора слов (рандомных строчных букв), разделенных пробелами.
Полный список парольных фраз системы вы найдете по кнопке Данные внизу вашей задачи
(одна строка из слов - одна парольная фраза).
Для обеспечения безопасности действующая парольная фраза не должна содержать двух слов,
являющихся анаграммами друг друга, то есть парольная фраза недействительна,
если буквы любого слова в парольной фразе можно переставить так,
чтобы образовать любое другое слово в парольной фразе. Сколько парольных фраз допустимо?
'''
from collections import Counter

def check_anagram(enter: str) -> bool:
    counter_list = [Counter(el) for el in enter.split()]
    for enum, i in enumerate(counter_list[:-1]):
        for j in counter_list[enum + 1:]:
            if i == j:
                return True
    return False


def testing():
    assert check_anagram('nyot babgr babgr kqtu kqtu kzshonp ylyk psqk') == True
    assert check_anagram('wchrl pzibt nvcae wceb') == False


def main():
    testing()

    with open(r'C:\my\Python_project\random_tasks\herokuapp\05.txt', 'r') as f:
        string_list = f.read().split('\n')[:-1]

    print(len([string for string in string_list if not check_anagram(string)]))


if __name__ == '__main__':
    main()
