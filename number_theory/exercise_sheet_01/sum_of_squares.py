#!/usr/bin/python

"""
For Number Theory SoSe 2021 Excersie Sheet 1 Exercise 2.

Find k = a^2 + b^2 and do prime decomposition.
"""

class SumOfSquares():
    def __init__(self, n):
        self.list_squares = [a ** 2 + b ** 2 for (a, b) in zip(range(1, n +1), range(1, n +1)) if a <= b]

    def print_list_squares(self):
        print(self.print_list_squares)

def main():
    obj = SumOfSquares(10)
    print(obj.list_squares)

if __name__ == "__main__":
    print(zip(range(1, 10 +1), range(1, 10 +1)))
    main()