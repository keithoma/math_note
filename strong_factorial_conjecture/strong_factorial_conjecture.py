"""Some computations regarding the strong factorial conjecture."""

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

def main():
    """Main."""
    print(lemma_2_17(10))


if __name__ == "__main__":
    main()
