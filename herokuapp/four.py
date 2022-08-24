'''
Вы пытаетесь разобраться в номерах отеля. Номера комнат хранятся в зашифрованном списке
(доступном по кнопке Данные) и часть номеров от комнат фиктивные и являются ловушками для воришек.
Каждая комната состоит из зашифрованного имени (строчные буквы, разделенные тире),
за которым следует тире, идентификатор сектора и контрольная сумма в квадратных скобках.
Комната реальная (а не фиктивная), если контрольная сумма представляет собой пять наиболее распространенных
букв в зашифрованном имени, расположенных по алфавиту. Например:
- aaaaa-bbb-z-y-x-123[abxyz] — это реальная комната,
потому что наиболее распространенными буквами являются a (5), b (3),
  а затем ничья между x, y и z, которые перечислены в алфавитном порядке.
- a-b-c-d-e-f-g-h-987[abcde] — это реальная комната, потому что, хотя все буквы связаны (по 1 каждой),
первые пять перечислены в алфавитном порядке.
- not-a-real-room-404[oarel] - реальная комната.
- totally-real-room-200[decoy] - комната ловушка.
У реальных комнат из списка выше сумма идентификаторов их секторов равна 1514.
Какова сумма идентификаторов секторов реальных комнат?
'''

from string import ascii_lowercase
from collections import Counter
import re

def decoder(enter: str) -> bool:
    code, pattern = enter[:-1].split('[')
    sim = [el for el in code if el in ascii_lowercase and el in pattern]
    group = {}
    for v, k in Counter(sim).items():
        group[k] = group.get(k, '') + v
    for val in group.values():
        check, pattern = pattern[:len(val)], pattern[len(val):]
        if not len(val) == len(check):
            if pattern:
                return False
            if not set(check) == set(val):
                return True

        if not sorted(val) == sorted(check):
            return False
    return True

def testing():
    assert decoder('aaaaa-bbb-z-y-x-123[abxyz]') == True
    assert decoder('a-b-c-d-e-f-g-h-987[abcde]') == True
    assert decoder('not-a-real-room-404[oarel]') == True
    assert decoder('totally-real-room-200[decoy]') == False
def main():
    testing()

    with open(r'C:\my\Python_project\random_tasks\herokuapp\04.txt', 'r') as f:
        indicators_list = f.read().split('\n')[:-1]

    room = [indicators for indicators in indicators_list if decoder(indicators)]
    print(sum(map(int, re.findall(r'\d+', '-'.join(room)))))

if __name__ == '__main__':
    main()
