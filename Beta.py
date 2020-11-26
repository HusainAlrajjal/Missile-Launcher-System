import random, time


# read datset from a txt file
def import_primes(address):
    dataset = list()
    file1 = open(address, "r")
    content = file1.read()
    records = content.split("\n")
    for i in records:
        dataset += i.split("\t")

    for i in range(len(dataset)):
        dataset[i] = int(dataset[i])

    file1.close()
    return dataset


address = "10000prime.txt"
primes = import_primes(address)


def fermat_primality_test(n, coprime_bases_list):
    pseudoprime_list = list()
    for i in coprime_bases_list:
        if modExp(i, n - 1, n) == 1:
            pseudoprime_list.append(i)
        else:
            print(n, "is not a prime.\t Reason: ", i)
            return False
    return pseudoprime_list


def gcd(a, b):
    if b == 0:
        return a
    elif a >= b:
        return gcd(b, modExp(a, 1, b))
    else:
        return gcd(b, a)


def ChineseRemainderTheoremSetup(n):
    # choosing a prime randomly from the dataset 1000prime.
    mk_list = list()
    m = 1
    for i in range(n):
        r = random.randint(0, len(primes) - 1)
        mk_list.append(primes[r])
        m *= mk_list[i]

    # choosing a where a is from  a mod mk
    a_list = list()
    i = 0

    # generate co-prime to mk
    while i < n:
        # problem 1: random number should be >= size(n digits
        r = random.randint(10 ** (len(str(mk_list[i])) - 1), mk_list[i] - 1)
        #
        if gcd(r, mk_list[i]) == 1:
            a_list.append(r)
            i += 1
    # end of generating co-primes of mk

    #
    Mk_list = list()
    for i in mk_list:
        Mk_value = m // i
        Mk_list.append(Mk_value)

    y_list = list()
    for i in range(n):
        y_list.append(multiplicativeInverse(Mk_list[i], mk_list[i]))

    X = 0
    # X is 23 and m = 105
    for i in range(n):
        X += Mk_list[i] * a_list[i] * y_list[i]
    X = X % m

    result = [X, mk_list]
    for i in range(n):
        result.append([a_list[i], mk_list[i]])
    return result


def modExp(b, n, m):
    n = str(bin(n))[2:]
    k = len(n)
    x = 1
    p = b % m
    n_list = list(range(k))
    n_list.reverse()
    for i in n_list:
        if n[i] == '1':
            x = (x * p) % m
        p = (p * p) % m
    return x


def multiplicativeInverse(a, m):
    a = a % m
    if gcd(a, m) == 1:
        # problem 2: [check] if a is not co-prime with m then there's no inverse
        for x in range(1, m):
            if (a * x) % m == 1:
                return x
    else:
        return "do sultan's magic way"
    return -1  # -1 indicates that there's no inverse for a mod m


def test(key, X, mlist):
    # this to ensure that the left pair of the key is less than the right pair of the key
    # we might check for the hacker and kick him out  this is the recording around [ 2: 30: 00 ]
    # key[0] = key[0] % key[1]

    for i in mlist:
        if key[1] == i:
            return (X % key[1]) == key[0]

    return False


def getRandom(n):
    return random.randint(10 ** (n - 1), (10 ** n) - 1)


def genAttack(nDigits, sizeOfAttack):
    attackKeys = []
    for i in range(sizeOfAttack):
        r = [getRandom(nDigits), getRandom(nDigits)]
        attackKeys.append(r)
    return attackKeys


def main():
    # n = int(input("Choose the number of Generals (n)>>> "))
    n = 5
    # result = ChineseRemainderTheoremSetup(n)
    # print(result)
    result = [2551626037209230983216, [98041, 13691, 42797, 1217, 60601], [79839, 98041], [10112, 13691],
              [10615, 42797], [1085, 1217], [47146, 60601]]
    SecretKey = result[0]
    mlist = result[1]

    for i in result[2:]:
        print(i, test(i, SecretKey, mlist))

    attackList = genAttack(5, 10000)

    for i in attackList:
        if test(i, SecretKey, mlist):
            print(i, "We have break your system :)")

    # print(test([79839, 98041], SecretKey, mlist))


if __name__ == '__main__':
    main()
