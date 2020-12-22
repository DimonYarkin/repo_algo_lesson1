"""
Задание 1.

Для каждой из трех задач выполнить следующее:

1) для каждой инструкции рядом в комментарии определите сложность этой инструкции
2) определите сложность алгоритма в целом

укажите сложность непосредственно в этом файле
точки, где нужно поработать вам, отмечены знаком '!!!'

Примечание:
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.
"""

import random


#############################################################################################
def check_1(lst_obj):
    """Функция должна создать множество из списка.

    Алгоритм 3:
    Создать множество из списка

    Сложность: O(n)
    """
    lst_to_set = set(lst_obj)  # O(len(...)) Зависит от величины списка примим сложность как O(n)
    return lst_to_set


#############################################################################################
def check_2(lst_obj):
    """Функция должная вернуть True, если все элементы списка различаются.

    Алгоритм 1:
    Проходимся по списку и для каждого элемента проверяем,
    что такой элемент отстутствует
    в оставшихся справа элементах

    Сложность:
    O(1) Прибовляем один раз потому что return в любом случае
    выполнется только один раз

    O(n)*O(1)+O(1) = O(n)
    Общая сложность функции O(n) - Линейная
    """
    for j in range(len(lst_obj)):          # O(n)
        if lst_obj[j] in lst_obj[j+1:]:    # O(1)
            return False                   # O(1)
    return True                            # O(1)


#############################################################################################
def check_3(lst_obj):
    """Функция должная вернуть True, если все элементы списка различаются.

    Алгоритм 2:
    Вначале выполним для списка сортировку, далее, сравниваем элементы попарно
    Если присутствуют дубли, они будут находиться рядом.

    Сложность: Расчет сложности
    O(n)+O(n log n) +O(n)*O(1)+O(1) =
    O(n + n log n +O(n*1)+1) =
    O(n + n log n +n+1 =
    O(n log n +2n +1) =
    O(n log n)
    Максимальная сложность это сортировка если список будет большой максимум времени займет сортировка

    """
    lst_copy = list(lst_obj)                 # O(len(...)) Зависит от длины списка примим как сложность O(n)
    lst_copy.sort()                          # O(n log n) Логарифмическая сложность для быстрой сортировки
    for i in range(len(lst_obj) - 1):        # O(n)
        if lst_copy[i] == lst_copy[i+1]:     # O(1) операции получения по индексу
            return False                     # O(1)
    return True                              # O(1)

#############################################################################################


for j in (50, 500, 1000, 5000, 1000):
    # Из 100000 чисел возьмем 'j' случайно выбранных
    # Всего 10 тыс. чисел
    lst = random.sample(range(-100000, 100000), j)

print(check_1(lst))
print(check_2(lst))
print(check_3(lst))
