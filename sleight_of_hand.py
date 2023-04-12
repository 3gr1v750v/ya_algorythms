# 81888427

from typing import List, Tuple


def read_input() -> Tuple[int, List[str]]:
    """Получение входных данных."""
    keys: int = int(input())
    numbers: List[str] = [str(input().strip()) for _ in range(4)]
    return keys, numbers


def calculate_score(numbers: List[str], keys: int) -> int:
    """
    Посчитать количество раз, сколько каждая цифра встречается в массиве.
    Сравнить all_player_keys с количеством повторений каждой цифры, и если оно
    больше или равно - прибавить балл.
    """
    score: int = 0
    all_player_keys: int = 2 * keys
    numbers_qty: List[int] = [0]*10

    for row in range(len(numbers)):
        for number in numbers[row]:
            if number != ".":
                numbers_qty[int(number)] += 1

    for qty in numbers_qty:
        if 0 < qty <= all_player_keys:
            score += 1

    return score


def main() -> None:
    """Функция запуска проекта."""
    keys, numbers = read_input()
    print(calculate_score(numbers, keys))


if __name__ == '__main__':
    main()
