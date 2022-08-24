'''
В многоквартирном доме вам нужно доставить товары во все квартиры,
но прежде товары нужно запаковать в коробки. Для этого нужно выяснить сколько квадратных футов картона вам нужно.
Коробка имеет форму правильной прямоугольной призмы и имеет длину l, ширину w, и высоту h.
На каждую коробку вам нужно:
2*l*w + 2*w*h + 2*h*l + площадь наименьшей стороны
Например:
- Для подарка размером 2x3x4 требуется 2*6 + 2*12 + 2*8 = 52
  квадратных футов оберточной бумаги плюс 6 квадратных футов по наименьшей стороне, итого
  итого 58 квадратных футов.
- Для подарка размером 1x1x10 требуется 2*1 + 2*10 + 2*10 = 42
  квадратных футов оберточной бумаги плюс 1 квадратный фут по наименьшей стороне, итого
  итого 43 квадратных фута.
Все числа в списке (кнопка данные) указаны в футах.
Сколько всего квадратных футов картона требуется для запаковки товаров?
'''
'''
Лента представляет собой наименьший периметр какой-либо одной грани. Каждой коробке так же требуется бантик из ленты,
количество футов ленты необходимое для банта равно кубическому футу объема подарка.'''

class Gift:
    def __init__(self, indicators):
        l, w, h = map(int, indicators.split('x'))
        self.l = l
        self.w = w
        self.g = h
        self.volume = l * w * h
        self.area_sides = (l * w, w * h, h * l)
        self.perimeters = (l + w, w + h, h + l)

    @property
    def calculate_cardboard(self):
        return (sum(self.area_sides) * 2) + min(self.area_sides)

    @property
    def calculate_lents(self):
        return (min(self.perimeters) * 2) + self.volume


# def calculate_cardboard(indicators: str) -> int:
#     l, w, h = map(int, indicators.split('x'))
#     sides = (l*w, w*h, h*l)
#     result = sum(map(lambda x: x*2, sides)) + min(sides)
#     return result


def tests():
    # assert calculate_cardboard('2x3x4') == 58
    # assert calculate_cardboard('1x1x10') == 43
    test_one = Gift('2x3x4')
    test_two = Gift('1x1x10')
    assert test_one.calculate_cardboard == 58
    assert test_two.calculate_cardboard == 43
    assert test_one.calculate_lents == 34
    assert test_two.calculate_lents == 14

def main():
    tests()

    with open(r'C:\my\Python_project\random_tasks\herokuapp\two.txt', 'r') as f:
        indicators_list = f.read().split('\n')[:-1]

    gift_list = [Gift(indicators) for indicators in indicators_list]
    print('Коробки', sum([obj.calculate_cardboard for obj in gift_list]))
    print('Ленты', sum([obj.calculate_lents for obj in gift_list]))




if __name__ == '__main__':
    main()
