from typing import List
import random


def comb(numbers: List[int]):
  length = len(numbers)
  gap = int(length / 1.3)
  swapped = True
  print(gap)

  while swapped or (gap >= 1):
    swapped = False
    for i in range(0, length - gap):
      print("i: {}, gap: {}, max: {}".format(i, gap, length - gap))
      if numbers[i] > numbers[i + gap]:
        print("n[{}]: {}, n[{}]: {}".format(i, numbers[i], i + gap, numbers[i + gap]))
        numbers[i], numbers[i + gap] = numbers[i + gap], numbers[i]
        print("n[{}]: {}, n[{}]: {}".format(i, numbers[i], i + gap, numbers[i + gap]))
        swapped = True
    gap = int(gap / 1.3)

  return numbers


if __name__ == '__main__':
  numbers = [random.randint(0, 100) for _ in range(7)]
  print(numbers)
  print(comb(numbers))
