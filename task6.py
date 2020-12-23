"""
Задание 6.
Задание на закрепление навыков работы со стеком

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте структуру "стопка тарелок".

Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.

Структура должна предусматривать наличие нескольких стеков.
Создание нового стека происходит при достижении предыдущим стеком порогового значения.
Реализуйте по аналогии с примером, рассмотренным на уроке, необходимые методы,
для реализации это структуры, добавьте новые методы (не рассмотренные в примере с урока)
для реализации этой задачи.

После реализации структуры, проверьте ее работу на различных сценариях
"""
from math import ceil


class StacksOfPlates:
    def __init__(self, plates_list, len_stacks):
        self.plates_list = plates_list
        self.len_stacks = len_stacks

    @property
    def arrange_the_stacks(self):
        part_len = ceil(len(self.plates_list) / self.len_stacks)
        return [self.plates_list[self.len_stacks * k:self.len_stacks * (k + 1)] for k in range(part_len)]


if __name__ == '__main__':
    plates = list(range(16))
    quantity_in_the_stack = 5
    stacksplates = StacksOfPlates(plates, quantity_in_the_stack)
    print(f'Исходный список тарелок\n {plates}')
    print(f'Количество в стопке = {quantity_in_the_stack}')
    print(f'Список сложенных стопок\n {stacksplates.arrange_the_stacks}')

    plates = list(range(25))
    quantity_in_the_stack = 3
    stacksplates = StacksOfPlates(plates, quantity_in_the_stack)
    print(f'Исходный список тарелок\n {plates}')
    print(f'Количество в стопке = {quantity_in_the_stack}')
    print(f'Список сложенных стопок\n {stacksplates.arrange_the_stacks}')
