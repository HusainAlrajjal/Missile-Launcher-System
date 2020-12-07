from itertools import combinations


def nCr(pair_list, r):
    pair_list = set(pair_list)
    comb = combinations(pair_list, r)
    return list(comb)


def main():
    pairs_list = list()
    pairs_list.append((1, 3))
    pairs_list.append((1, 2))
    pairs_list.append((1, 56))

    pairs_list.append((1, 3))

    print(nCr(pairs_list, 3))


if __name__ == '__main__':
    main()
