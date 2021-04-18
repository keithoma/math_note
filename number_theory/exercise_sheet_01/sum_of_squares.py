#!/usr/bin/python

"""
For Number Theory SoSe 2021 Excersie Sheet 1 Exercise 2.

Find k = a^2 + b^2 and do prime decomposition.
"""

class SumOfSquares():
    def __init__(self, n):
        self.list_squares = [a ** 2 + b ** 2 for a in range(1, n + 1) for b in range(1, n + 1) if a <= b]
        self.sum_of_squares = [[a, b] for a, b in zip(self.list_squares, [prime_factors(n) for n in self.list_squares])]

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def main():
    obj = SumOfSquares(10)
    print(obj.list_squares)
    print(obj.sum_of_squares)

if __name__ == "__main__":
    print(zip(range(1, 10 +1), range(1, 10 +1)))
    main()