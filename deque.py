# 82682424

from typing import List, Optional, Union


class OverFlowError(Exception):
    """Ошибка переполнения очереди."""
    pass


class EmptyDeque(Exception):
    """Очередь пуста."""
    pass


class DequeQueue:
    """Дек очередь с кольцевым буфером."""
    def __init__(self, queue_length: int):
        self.__queue: List[Optional[int]] = [None] * queue_length
        self.__max_queue_length: int = queue_length
        self.__head: int = 0
        self.__tail: int = 0
        self.__queue_size: int = 0

    def __check_is_empty(self) -> bool:
        """Проверка на наличие записей в очереди."""
        return self.__queue_size == 0

    def __check_is_full(self) -> bool:
        """Проверка на переполнение очереди."""
        return self.__queue_size == self.__max_queue_length

    def __index_calculation(self, position: int, flag: bool) -> int:
        """Расчет индекса смещения позиции очереди."""
        if flag:
            return (position + 1) % self.__max_queue_length
        else:
            return (position - 1) % self.__max_queue_length

    def push_front(self, x: Union[int, None]) -> None:
        """Добавление записи в начало очереди."""
        if self.__check_is_full():
            raise OverFlowError
        if self.__queue[self.__head] is None:
            self.__tail = self.__index_calculation(self.__tail, True)
        else:
            self.__head = self.__index_calculation(self.__head, False)
        self.__queue[self.__head] = x
        self.__queue_size += 1

    def push_back(self, x: Union[int, None]) -> None:
        """Добавление записи в конец очереди"""
        if self.__check_is_full():
            raise OverFlowError
        self.__queue[self.__tail] = x
        self.__tail = self.__index_calculation(self.__tail, True)
        self.__queue_size += 1

    def pop_front(self) -> Union[int, None]:
        """Получение и удаление значения из начала очереди."""
        if self.__check_is_empty():
            raise EmptyDeque
        x = self.__queue[self.__head]
        self.__queue[self.__head] = None
        self.__head = self.__index_calculation(self.__head, True)
        self.__queue_size -= 1
        return x

    def pop_back(self) -> Union[int, None]:
        """Получение и удаление значения из конца очереди."""
        if self.__check_is_empty():
            raise EmptyDeque
        self.__tail = self.__index_calculation(self.__tail, False)
        x = self.__queue[self.__tail]
        self.__queue[self.__tail] = None
        self.__queue_size -= 1
        return x


def run_deque_method(deque, command) -> str:
    """Управление и исполнение методов класса деки."""
    cmd, *args = command.split()
    action = getattr(deque, cmd)
    try:
        return action() if not args else action(int(args[0]))
    except AttributeError:
        raise AttributeError(f"Неподдерживаемая команда '{cmd}'.")
    except (OverFlowError, EmptyDeque):
        return 'error'


def main():
    """Функция запуска проекта."""
    commands_qty = int(input())
    queue_length = int(input())
    deque = DequeQueue(queue_length)

    for _ in range(commands_qty):
        command = input()
        result = run_deque_method(deque, command)
        if result is not None:
            print(result)


if __name__ == '__main__':
    main()
