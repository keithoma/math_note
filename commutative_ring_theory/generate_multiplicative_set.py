class QuotientRing:
    def __init__(self, n) -> None:
        self.n = n

    def make_next_products(self, generating_set):
        next = set()
        for x in generating_set:
            for y in generating_set:
                if (x * y) % self.n in generating_set:
                    check = ""
                else:
                    check = "new"
                # print("{} * {} = {} ~ {} mod {} {}".format(x, y, x * y, (x * y) % self.n, self.n, check))
                next.add((x * y) % self.n)
        # print("next generators: {}".format(next))
        # print(next)
        return next

    def generate(self, generating_set):
        original = generating_set.copy()
        while True:
            next_generators = self.make_next_products(generating_set)
            if not generating_set == next_generators:
                generating_set.update(next_generators)
            else:
                break
        print("{}     =>     {}".format(original, generating_set))
        return generating_set

    def power_set(self):
        pass # i got lazy


def main():

    # residue_3 = QuotientRing(3)
    # residue_3.generate({1, 2})

    # residue_4 = QuotientRing(4)
    # residue_4.generate({1, 2, 3})

    # residue_5 = QuotientRing(5)
    # residue_5.generate({1, 3, 4})

    # residue_6 = QuotientRing(6)
    # residue_6.generate({1, 4, 5})

    # residue_7 = QuotientRing(7)
    # residue_7.generate({1, 4, 6})

    residue_12 = QuotientRing(12)
    
    for n in range(3, 12):
        residue_12.generate({1, 2, n})
if __name__ == "__main__":
    main()

