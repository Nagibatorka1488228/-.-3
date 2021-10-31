import random
from random import randint

def find_missing_nums(nums):
  norm = [a for a in range(1, len(nums)+1)]
  f = []
  for r in norm:
    if r not in nums:
      f.append(r)
  return f

n = int(input())
nums = [randint(1, n) for i in range(n)]

print(find_missing_nums(nums))
