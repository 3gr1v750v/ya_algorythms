# 82681998

from typing import Callable, Dict, List


OPERATORS: Dict[str, Callable[[int, int], int]] = {
    "+": (lambda x, y: x + y),
    "-": (lambda x, y: x - y),
    "*": (lambda x, y: x * y),
    "/": (lambda x, y: x // y)
}


class Stack:
    """Класс стека объектов."""
    def __init__(self) -> None:
        self.__items: List[int] = []

    def push(self, item: int) -> None:
        self.__items.append(item)

    def pop(self) -> int:
        try:
            return self.__items.pop()
        except IndexError:
            raise IndexError('Отсутствуют входящие данные.')


def read_input() -> List[str]:
    """Получение входящих данных."""
    calculation_elements: List[str] = list(input().strip().split())
    return calculation_elements


def calculator(input) -> int:
    """Вычисление результата операции с использованием польской нотации."""

    stack = Stack()

    for element in input:
        if element not in OPERATORS:
            try:
                stack.push(int(element))
            except ValueError:
                raise ValueError(f'Параметр "{element}" не поддерживается.')
        else:
            x, y = stack.pop(), stack.pop()
            try:
                calculation_result: int = OPERATORS[element](y, x)
            except ZeroDivisionError:
                raise ZeroDivisionError('Деление на ноль недоступно.')
            stack.push(calculation_result)

    return stack.pop()


def main() -> None:
    """Функция запуска проекта."""
    calculation_elements = read_input()
    print(calculator(calculation_elements))


if __name__ == '__main__':
    main()
