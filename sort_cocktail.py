from typing import List
import random


def cocktail(numbers: List[int]) -> List[int]:
  end = len(numbers) - 1
  start = 0
  swapped = True

  def swap(start: int, end: int, numbers: List[int], reverse: bool = False):
    ret = False
    for i in range(start, end, -1 if reverse else 1):
      if numbers[i] > numbers[i + 1]:
        numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
        ret = True
        print('swap {} {}'.format(numbers[i], numbers[i + 1]))
    return ret

  while swapped:
    swapped = False
    print('0:start={}, end={}'.format(start, end))
    swapped = swap(start, end, numbers)
    end = end - 1
    if not swapped:
      break
    print('1:start={}, end={}'.format(start, end))
    swapped = swap(end - 1, start - 1, numbers, True)
    start = start + 1

  return numbers


if __name__ == '__main__':
  numbers = [random.randint(0, 100) for _ in range(10)]
  print(numbers)
  print(cocktail(numbers))
