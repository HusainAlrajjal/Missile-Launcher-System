from itertools import combinations


def nCr(pair_list, r, n):
    pair_list = set(pair_list)
    comb = list()
    for i in range(r, n + 1):
        comb += combinations(pair_list, i)
    return list(comb), len(list(comb))


def main():
    pairs_list = list()
    pairs_list.append((1, 3))
    pairs_list.append((1, 2))
    pairs_list.append((1, 56))
    pairs_list.append((1, 58))
    pairs_list.append((1, 76))

    pairs_list.append((1, 3))

    print(nCr(pairs_list, 5, 5))


if __name__ == '__main__':
    main()
