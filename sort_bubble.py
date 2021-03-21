from typing import List
import random


def bubble(numbers: List[int]) -> List[int]:
  for limit in range(len(numbers), 0, -1):
    for i in range(0, limit - 1):
      if numbers[i] > numbers[i + 1]:
        first, second = numbers[i], numbers[i + 1]
        numbers[i], numbers[i + 1] = second, first
  return numbers


if __name__ == '__main__':
  nums = [random.randint(0, 1000) for _ in range(10)]
  print(nums)
  print(bubble(nums))
