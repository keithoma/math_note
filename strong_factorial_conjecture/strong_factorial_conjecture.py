"""Some computations regarding the strong factorial conjecture."""

from sympy import *

def lemma_2_17(n):
    """Computes the coefficients defined recursively in lemma 2.17."""
    list_of_c = [1, 1]

    def pair_sums_to(k):
        pairs = [
            (list_of_c[i], list_of_c[j])
            for i in range(k + 1) for j in range(k + 1) if i + j == k
        ]
        return pairs

    def c(k):
        pairs = pair_sums_to(k - 1)

        result = 0
        for a, b in pairs:
            result = result + a * b
        return result

    for i in range(2, n + 1):
        list_of_c.append(c(i))

    return list_of_c


def fps_inverse():
    a = fps(3 + x)
    print(a)
    inv = a.inverse(6)
    print(inv)
    result = compute_fps(inv)
    print(result)

def multinomial_theorem():
    x = symbols('x')
    a = IndexedBase('a')
    b = IndexedBase('b')
    i = symbols('i', cls=Idx)

    f = a[0] + a[1] * x + a[2] * x ** 2 + a[3] * x ** 3 + a[4] * x ** 4
    g = b[0] + b[1] * x + b[2] * x ** 2 + b[3] * x ** 3 + b[4] * x ** 4
    result = f.subs(x, g)

    print(latex(expand(result)))



def main():
    """Main."""
    # print(lemma_2_17(10))
    # fps_inverse()
    multinomial_theorem()

if __name__ == "__main__":
    main()
