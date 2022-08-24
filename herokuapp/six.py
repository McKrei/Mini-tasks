'''
Вам удалось проникнуть в лабораторию по производству волшебного зелья. Вы сканируете химический состав зелья и обнаруживаете, что он состоит из чрезвычайно длинных полимеров (Ваши данные полимера вы найдете по кнопке Данные внизу задачи).
Полимер состоит из более мелких звеньев, которые при срабатывании реагируют друг с другом так, что разрушаются два соседних звена одного типа и противоположной полярности. Типы звеньев обозначаются буквами; полярность единиц представлена ​​заглавными буквами. Например, r и R — единицы одного типа, но противоположной полярности, тогда как r и s — совершенно разные типы и не реагируют.
Например:
aA     - a и A реагируют, ничего не оставляя после себя.
abBA   - bB уничтожает себя, оставляя aA. Как и выше, aA затем уничтожает себя, не оставляя ничего.
abAB   - нет двух смежных единиц одного типа, поэтому ничего не происходит.
aabAAB - несмотря на то, что aa и AA одного типа, их полярности совпадают, поэтому ничего не происходит.
Теперь рассмотрим более крупный пример, dabAcCaCBAcCcaDA:
dabAcCaCBAcCcaDA    - первый 'cC' удаляется;
dabAaCBAcCcaDA      - это создает 'Aa', который удаляется;
dabCBAcCcaDA        - либо 'cC', либо 'Cc' удаляются (результат тот же).
dabCBAcaDA          - дальше реакции нет
Один из типов звеньев вызывает проблемы; это предотвращает разрушение полимера настолько, насколько это необходимо. Ваша цель — выяснить, какой тип блока вызывает больше всего проблем, удалить все его экземпляры (независимо от полярности), полностью прореагировать с оставшимся полимером и измерить его длину.

Например, снова используя полимер dabAcCaCBAcCcaDA из приведенного выше:
Удаление всех модулей A/a создает dbcCCBcCcD. После реакции полимер остается таким dbCBcD, который имеет длину 6.
Удаление всех блоков B/b дает daAcCaCAcCcaDA. После реакции полимер остается таким daCAcaDA, длина которого равна 8.
Удаление всех блоков C/c производит dabAaBAaDA. После реакции полимер остается таким daDA, длина которого равна 4.
Удаление всех единиц D/d дает abAcCaCBAcCcaA. После реакции полимер остается таким abCBAc, длина которого равна 6.

В этом примере лучше удалить все блоки C/c, что даст ответ 4.
Какова длина самого короткого полимера, который вы можете получить, удалив все звенья ровно одного типа и полностью прореагировав в результате?
'''
def foo(result_string:str, elements_un: list[str]) -> int:
    changes = True
    while changes == True:
        changes = False
        l = len(result_string)
        for letter in elements_un:
            pattern = (letter * 2).capitalize()
            result_string = result_string.replace(pattern, '')
            result_string = result_string.replace(pattern[::-1], '')
        if l != len(result_string):
            changes = True

    return len(result_string)


def testing(elements_string):
    assert min_formula(elements_string) == 4

def min_formula(elements_string:str) -> int:
    elements_un = set(elements_string.lower())
    print(elements_un)
    result_list = [foo(elements_string, elements_un)]
    for letter in elements_un:
        check_sting = elements_string.replace(letter, '').replace(letter.title(), '')
        l = foo(check_sting, elements_un)
        result_list.append(l)
        print(letter, l)

    return min(result_list)


def main():
    testing('dabAcCaCBAcCcaDA')

    with open(r'C:\my\Python_project\random_tasks\herokuapp\06.txt', 'r') as f:
        elements_string = f.read()

    print(min_formula(elements_string[:-1]))


if __name__ == '__main__':
    main()
