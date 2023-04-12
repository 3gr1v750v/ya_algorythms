# 83764475

import random
from dataclasses import dataclass
from typing import List, Optional, Tuple


@dataclass
class Member:
    """Запись данных участников."""
    __slots__ = ('name', 'score', 'penalty')

    name: str
    score: int
    penalty: int

    def __post_init__(self):
        self.score = int(self.score)
        self.penalty = int(self.penalty)

    @property
    def assertion_value(self) -> Tuple[int, int, str]:
        """Изменение порядка и знаков элементов данных, для сравнения."""
        return (-self.score, self.penalty, self.name)

    def __le__(self, other) -> bool:
        """
        Реализация сравнения комбинации свойств класса для последующего
        использования для сортировки объектов класса в массиве.
        Сортировка предполагает, что при сравнении двух объектов выше будет
        идти тот, у которого больше значение score (по этой причине знак score
        меняется на отрицательный при сравнении двух объектов). При равенстве
        числа score первым будет объект с меньшим penalty. Если же
        и penalty совпадают, то первым будет тот, у которого name идёт раньше
        в алфавитном (лексикографическом) порядке.
        """
        return self.assertion_value <= other.assertion_value

    def __str__(self) -> str:
        return self.name


def quick_sort(
        array: List[Member],
        start: int = 0,
        stop: Optional[int] = None) -> None:
    """Рекурсивная функция осуществляющая сортировку массива по возрастанию."""
    if stop is None:
        stop = len(array) - 1

    if start >= stop:
        return

    pivot_index: int = partition_rand(array, start, stop)

    quick_sort(array, start, pivot_index - 1)
    quick_sort(array, pivot_index + 1, stop)


def partition_rand(array: List[Member], start: int, stop: int) -> int:
    """
    Генерация рандомного индекса опорной точки, лежащей между индексами
    начала и конца массива.

    1) Присваиваем для pivot рандомного значение индекса.
    2) Меняем местами позиции первого элемента в массиве на рандомный элемент,
    что необходимо для функции partition, которая начинает отсчёт с первого
    элемента.
    3) Запускаем функцию разделения массива с нахождением опорной точки.
    """
    rand_pivot: int = random.randrange(start, stop)

    array[start], array[rand_pivot] = array[rand_pivot], array[start]
    return partition(array, start, stop)


def partition(array: List[Member], start: int, stop: int) -> int:
    """
    Функция проходит по массиву в диапазоне от start до stop, меняя
    элементы местами таким образом, что опорный элемент pivot, занимает
    такое место в массиве, что слева от него находятся значения меньше pivot,
    а справа - больше. Функция возвращает новый индекс pivot (позиция
    в массиве, на которую переместится pivot).

    1) Первый элемент списка (ранее рандомно выбранный) становится опорной
    точкой.
    2) Проходим по элементам массива, сравнивая каждый из них с опорным
    элементом. Счетчик i указыват на элемент, который больше опорного элемента
    и должен быть перемещен в правую часть массива.
    Если условие сравнения выполняется успешно, то элемент перемещается в левую
    часть списка, меняясь местами с элементом с индексом i (который большое
    опорного элемента).
    3) В конце цикла меняем местами опорный элемент и крайний элемент, у
    которого произошла перемена мест в массиве. Т.к. он попал под условие
    <элемент в массиве> <= <опорный элемент> и надо чтобы значения меньше
    опорного элемента хранились в левой части списка.
    """
    pivot: int = start
    i: int = start + 1

    for j in range(start + 1, stop + 1):
        if array[j] <= array[pivot]:
            array[i], array[j] = array[j], array[i]
            i += 1

    array[pivot], array[i - 1] = array[i - 1], array[pivot]
    pivot = i - 1
    return pivot


def read_input() -> List[Member]:
    """Чтение входящих данных."""
    member_qty: int = int(input())
    members: List[Member] = [
        Member(*input().split()) for _ in range(member_qty)
    ]
    return members


def main() -> None:
    """Драйвер программы."""
    members: List[Member] = read_input()
    quick_sort(members)
    print(*members, sep='\n')


def test():
    """Тестирование программы."""
    members = [
        Member("alla", 4, 100),
        Member("gena", 6, 1000),
        Member("gosha", 2, 90),
        Member("rita", 2, 90),
        Member("timofey", 4, 80),
    ]
    quick_sort(members)
    assert str(members[0]) == "gena"
    assert str(members[1]) == "timofey"
    assert str(members[2]) == "alla"
    assert str(members[3]) == "gosha"
    assert str(members[4]) == "rita"


if __name__ == "__main__":
    main()
