# 81888334

from typing import List, Tuple


def read_input() -> Tuple[List[int], int]:
    """Получение данных."""
    street_length: int = int(input())
    street: List[int] = [int(num) for num in input().strip().split()]
    return street, street_length


def print_distance(street: List[int], street_length: int) -> List[int]:
    """Определение дистанции в списке до ближайшего нуля."""
    nearest_zero: List[int] = [0]*street_length

    if street[0] != 0:
        nearest_zero[0] = street_length

    for i in range(1, street_length):
        if street[i] != 0:
            nearest_zero[i] = nearest_zero[i - 1] + 1

    for i in range(street_length-2, -1, -1):
        if street[i] != 0:
            nearest_zero[i] = min(nearest_zero[i], nearest_zero[i + 1] + 1)

    return nearest_zero


def main() -> None:
    """Функция запуска проекта."""
    street, street_length = read_input()
    print(' '.join(str(num) for num in print_distance(street, street_length)))


if __name__ == '__main__':
    main()
