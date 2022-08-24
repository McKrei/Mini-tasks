'''
Вы находитесь в городе, где все дома и улицы образуют идеальную сетку,
чтобы пройти из пункта А в пункт B вы можете ходить только по улицам и перекресткам,
нет никаких переулков, чтобы сократить путь по диагонали или около того.
У вас есть документ (доступный по нажатию кнопки Данные) с инструкциями с помощью которых вы можете прийти в дом,
где проходит вечеринка. В документе указано, что вы должны начать с заданных координат
(где вы находитесь сейчас) и смотреть на север. Затем следуйте указанной последовательности:
поверните налево (L) или направо (R) на 90 градусов, затем пройдите вперед заданное количество блоков,
закончив на новом перекрестке.К сожалению, инструкции написаны не оптимально и если вы им будете
следовать — то не успеете на вечеринку. Учитывая, что ходить можно только по сетке улиц города,
как далеко находится кратчайший путь до вечеринки?
Например:
 - Следуя за R2, L3 оставляет вас в 2 кварталах на восток и 3 кварталах на север или в 5 кварталах от вас.
 - R2, R2, R2 оставляет вас в 2 кварталах к югу от вашей начальной позиции, которая находится в 2 кварталах от вас.
 - R5, L5, R5, R3 оставляет вас в 12 кварталах от вас.
'''

class Orientation:
    cardinal_directions = ('x+', 'y+', 'x-', 'y-')
    orientation = 'x+'

    @property
    def turn_right(self):
        i = self.cardinal_directions.index(self.orientation)
        self.orientation = self.cardinal_directions[i + 1] if i < 3 else self.cardinal_directions[0]

    @property
    def turn_left(self):
        i = self.cardinal_directions.index(self.orientation)
        self.orientation = self.cardinal_directions[i - 1]


class GeoLocation:
    x = 0
    y = 0
    view = Orientation()

    def go(self, step):
        self.view.turn_right if step[0] == 'R' else self.view.turn_left
        sign = self.view.orientation[1]
        if self.view.orientation[0] == 'x':
            self.x = eval(f"{self.x} {sign} {step[1:]}")
        else:
            self.y = eval(f"{self.y} {sign} {step[1:]}")


    def distance_to_start(self):
        return abs(self.x) + abs(self.y)


# with open('01.txt', 'r') as file:
#     steps_list = file.read().split(', ')





def main():
    steps_list = 'L1, L3, L5, L3, R1, L4, L5, R1, R3, L5, R1, L3, L2, L3, R2, R2, L3, L3, R1, L2, R1, L3, L2, R4, R2, L5, R4, L5, R4, L2, R3, L2, R4, R1, L5, L4, R1, L2, R3, R1, R2, L4, R1, L2, R3, L2, L3, R5, L192, R4, L5, R4, L1, R4, L4, R2, L5, R45, L2, L5, R4, R5, L3, R5, R77, R2, R5, L5, R1, R4, L4, L4, R2, L4, L1, R191, R1, L1, L2, L2, L4, L3, R1, L3, R1, R5, R3, L1, L4, L2, L3, L1, L1, R5, L4, R1, L3, R1, L2, R1, R4, R5, L4, L2, R4, R5, L1, L2, R3, L4, R2, R2, R3, L2, L3, L5, R3, R1, L4, L3, R4, R2, R2, R2, R1, L4, R4, R1, R2, R1, L2, L2, R4, L1, L2, R3, L3, L5, L4, R4, L3, L1, L5, L3, L5, R5, L5, L4, L1, R1, L2, L4, L2, L4, L1, R4, R4, R5, R1, L4, R2, L3, L2, L4, R2, L4, L1, L2, R1, R4, R3, R2, R2, R5, L1, L2'.split(', ')
    me = GeoLocation()
    for step in steps_list:
        me.go(step)
        print(step, ':', me.x, me.y)

    print(f'{me.x = }, {me.y = }\n{me.distance_to_start()}')

if __name__ == '__main__':
    main()
