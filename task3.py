"""
Задание 3.

Для этой задачи:
1) придумайте 1-3 решения (желательно хотя бы два)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.


Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.
"""
''' 
1) Расчет сложности функции top_company(mydic)
O(1) + O(n log n) + O(1)
=O(1 + n log n + 1)
=O(n log n)
Максимальная сложность функции O(n log n) 
Вывод сложность всей функции O(n log n) - Логорифмическая

2) Расчет сложности функции top_company_v2(mydic)
O(1) + O(n) * O(n) * O(1) + O(1) + O(1) + O(1) + O(1)
=O(1 + n * n * 1 + 1 + 1 + 1)
=O(n^2)

Максимальная сложность функции O(n^2) 
Вывод сложность всей функции O(n^2) - Квадратичный

'''


def top_company(mydic):
    list_dic = list(mydic.items())  # O(1)
    list_us_sort = sorted(list_dic, key=lambda i: i[1], reverse=True)  # O(n log n)
    return list_us_sort[0:3]  # O(1)


def top_company_v2(mydic):
    list_top = []  # O(1)
    for i in range(3):  # O(n)
        list_max = ['', 0]  # O(1)
        for num, key in enumerate(mydic):  # O(n)
            if list_max[1] < mydic[key]:  # O(1)
                list_max = [key, mydic[key]]  # O(1)
        list_top.append(list_max)  # O(1)
        mydic.pop(list_max[0])  # O(1)
    return list_top  # O(1)


if __name__ == '__main__':
    mydic = {'фирма1': 20000,
             'фирма2': 10000,
             'фирма3': 30000,
             'фирма4': 120000,
             'фирма5': 25000,
             'фирма6': 50000}

    print(f'Резкльтат первого решения {top_company(mydic)}')
    print(f'Резкльтат второго решения {top_company_v2(mydic)}')
