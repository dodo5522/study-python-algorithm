from typing import List
import random


def sort(numbers: List[int]) -> List[int]:
  for i in range(0, len(numbers) - 1):
    min_idx = i
    for j in range(i + 1, len(numbers)):
      if numbers[min_idx] > numbers[j]:
        min_idx = j
    if numbers[i] != numbers[min_idx]:
      numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]
  return numbers


if __name__ == '__main__':
  numbers = [random.randint(0, 100) for _ in range(10)]
  print(numbers)
  print(sort(numbers))
