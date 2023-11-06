#!/usr/bin/env python3

FILE = "IntegerArray.txt"

def read_file(name):
  list = []
  with open(name) as f:
    for line in f:
      list.append(int(line))
  return list

def merge_and_count_split(B, C):
  splits = 0
  i = j = 0
  D = []

  while i < len(B) and j < len(C):
    if B[i] <= C[j]:
      D.append(B[i])
      i += 1
    else:
      D.append(C[j])
      splits += len(B) - i
      j += 1

  while i < len(B):
    D.append(B[i])
    i += 1
  while j < len(C):
    D.append(C[j])
    splits += len(B) - i
    j += 1

  return D, splits

def sort_and_count(A):
  if len(A) <= 1:
    return A, 0
  elif len(A) == 2:
    if A[0] > A[1]:
      R = [A[1], A[0]]
      return R, 1
    else:
      return A, 0
  else:
    half = len(A) // 2
    B, x = sort_and_count(A[:half])
    C, y = sort_and_count(A[half:])
    D, z = merge_and_count_split(B, C)
    return D, (x + y + z)

def main():
  unsorted_list = read_file(FILE)
  print(sort_and_count(unsorted_list))
