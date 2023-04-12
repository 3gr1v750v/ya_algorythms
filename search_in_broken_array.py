# 83554935

from typing import List, Optional


def broken_search(
        nums: List[int],
        target_val: int,
        left: int = 0,
        right: Optional[int] = None) -> int:
    """
    Поиск индекса значения в обычном массиве состоящим из скопированных
    данных кольцевого буфера, но со сдвинутой исходной
    отсортированной последовательностью.
    Пример массива: [19, 21, 100, 101, 1, 4, 5, 7, 12].
    """

    if right is None:
        right = len(nums) - 1

    if right < left:
        return - 1

    mid: int = (left + right) // 2

    if nums[mid] == target_val:
        return mid

    if nums[left] <= nums[mid]:
        if nums[left] <= target_val < nums[mid]:
            return broken_search(nums, target_val, left, mid - 1)
        return broken_search(nums, target_val, mid + 1, right)
    else:
        if nums[mid] < target_val <= nums[right]:
            return broken_search(nums, target_val, mid + 1, right)
        return broken_search(nums, target_val, left, mid - 1)


def broken_search_test():
    """Тестирование программы."""
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6


if __name__ == '__main__':
    broken_search_test()
