#!/usr/bin/env python3

'''
You are given as input an unsorted array of n distinct numbers, where n is a power of 2.
Give an algorithm that identifies the second-largest number in the array,
and that uses at most n + log2n - 2 comparisons.
'''

'''
Strategy: Divide and conquer. Return top element plus list of alternates. (n-1 comps)
Then recurse through list of alternates. (log2n - 1 comps)
'''

FILE = "IntegerArray.txt"

def read_file(name):
  list = []
  with open(name) as f:
    for line in f:
      list.append(int(line))
  return list

def recurse(list):
  if len(list) == 1:
    return list[0], [0]
  elif len(list) == 2:
    if list[0] > list[1]: # 1 comparison
      return list[0], [list[1]]
    else:
      return list[1], [list[0]]
  else:
    half = len(list) // 2
    a1, b1 = recurse(list[:half])
    a2, b2 = recurse(list[half:])
    if a1 > a2: # 1 comparison
      b1.append(a2)
      return a1, b1
    else:
      b2.append(a1)
      return a2, b2

def main():
  unsorted_list = read_file(FILE)
  top, list = recurse(unsorted_list)
  second, _ = recurse(list)
  print(top,second)
