#!/usr/bin/env python3

def length(x):
  l = 0
  while x >= 1:
    l = l + 1
    x = x / 10
  return l

def split(x,m):
  a = x // (10**m)
  b = x % (10**m)
  return a,b

def multiply(x,y):
  n = max(length(x),length(y))
  m = n // 2
  if n < 2:
    return x*y
  else:
    a,b = split(x,m)
    c,d = split(y,m)
    ac = multiply(a,c)
    bd = multiply(b,d)
    i = multiply(a+b,c+d)
    j = i - ac - bd
#    print(a,b,c,d,ac,bd,i,j,m,n)
    return (ac * 10**(2*m)) + (j * 10**m) + bd

def main():
  print(multiply(int(input("num1 ")),int(input("num2 "))))


# This is GPT4 generated code, I took from it the `n // 2` notion.
# Previously I was using `int(n/2)` but this resulted in some
# incorrect splitting.
def karatsuba(x, y):
    """
    Multiply two integers using Karatsuba algorithm.
    """
    # Base case for the recursion
    if x < 10 and y < 10:  # single-digit numbers
        return x * y

    # Calculate the size of the numbers
    n = max(len(str(x)), len(str(y)))
    m = n // 2

    # Split the numbers in half
    a, b = divmod(x, 10**m)
    c, d = divmod(y, 10**m)

    # Recursively compute the three products
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_plus_bc = karatsuba(a + b, c + d) - ac - bd

    # Combine the three products to get the final result
    return ac * 10**(2*m) + ad_plus_bc * 10**m + bd

