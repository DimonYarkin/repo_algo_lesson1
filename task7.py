"""
Задание 7.
Задание на закрепление навыков работы с очередью

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте структуру "доска задач".


Структура должна предусматривать наличие несольких очередей задач, например
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения

После реализации структуры, проверьте ее работу на различных сценариях

"""


class TaskBoard:
    def __init__(self):
        self.task_base = []
        self.task_work = []
        self.task_complite = []

    # Проверка очередей на пустоту
    def is_empty_task_base(self):
        return self.task_base == []

    def is_empty_task_work(self):
        return self.task_work == []

    def is_empty_task_complite(self):
        return self.task_complite == []

    # ++++++++++++++++++++++++++++++++++
    # Процедуры добавления в очереди
    def to_queue_task_base(self, item):
        self.task_base.insert(0, item)

    def to_queue_task_work(self, item):
        self.task_work.insert(0, item)

    def to_queue_task_complite(self, item):
        self.task_complite.insert(0, item)

    # +++++++++++++++++++++++++++++++++++++
    # Излечение элементов из очередей

    def from_queue_task_base(self):
        return self.task_base.pop()

    def from_queue_task_work(self):
        return self.task_work.pop()

    def from_queue_task_complite(self):
        return self.task_complite.pop()

    # ++++++++++++++++++++++++++++++++++++
    # Размеры очередей

    def size_task_base(self):
        return len(self.task_base)

    def size_task_work(self):
        return len(self.task_work)

    def size_task_complite(self):
        return len(self.task_complite)


if __name__ == '__main__':
    task_board = TaskBoard()
    # Добавим задачи в базовую очередь
    task_board.to_queue_task_base('Задача 1')
    task_board.to_queue_task_base('Задача 2')
    task_board.to_queue_task_base('Задача 3')

    print(
        f'Состав базовой очереди {task_board.task_base} размер очереди {task_board.size_task_base()} проверка что очередь не пустая {task_board.is_empty_task_base()}')
    # Извлечем 2 элемента из очереди и поместим его в очередь на доработку
    task_board.to_queue_task_work(task_board.from_queue_task_base())
    task_board.to_queue_task_work(task_board.from_queue_task_base())

    print(
        f'Состав очереди на доработку {task_board.task_work} размер очереди {task_board.size_task_work()} проверка что очередь не пустая {task_board.is_empty_task_work()}')
    print(
        f'Состав базовой очереди {task_board.task_base} размер очереди {task_board.size_task_base()} проверка что очередь не пустая {task_board.is_empty_task_base()}')

    # Извлечем элемент из очереди на доработку и поместим в очередь выполнено
    task_board.to_queue_task_complite(task_board.from_queue_task_work())
    print(
        f'Состав очереди выполнено {task_board.task_complite} размер очереди {task_board.size_task_complite()} проверка что очередь не пустая {task_board.is_empty_task_complite()}')
    print(
        f'Состав очереди на доработку {task_board.task_work} размер очереди {task_board.size_task_work()} проверка что очередь не пустая {task_board.is_empty_task_work()}')
