'''
Акростих — осмысленный текст, сложенный из начальных букв каждой строки стихотворения.
Акроним — вид аббревиатуры, образованной начальными звуками (напр. НАТО, вуз, НАСА, ТАСС), которое можно произнести слитно (в отличие от аббревиатуры, которую произносят «по буквам», например: КГБ — «ка-гэ-бэ»).
На вход даётся текст. Выведите слитно первые буквы каждого слова. Буквы необходимо выводить заглавными.
Эту задачу можно решить в одну строчку.
'''
import re

foo = lambda s: ''.join(re.findall(r'\b\w', s)).upper()

assert foo('Московский государственный институт международных отношений') == 'МГИМО'
assert foo('микоян авиацию снабдил алкоголем, народ доволен работой авиаконструктора') == 'МАСАНДРА'

print('Тесты прошел!')