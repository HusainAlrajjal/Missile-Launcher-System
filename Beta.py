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
    mk_list = list()
    m = 1
    for i in range(n):
        r = random.randint(0, len(primes) - 1)
        mk_list.append(primes[r])
        m *= mk_list[i]
    a_list = list()
    i = 0
    while i < n:
        r = random.randint(1, mk_list[i] - 1)
        if gcd(r, mk_list[i]) == 1:
            a_list.append(r)
            i += 1
    y_list = list()
    Mk_list = list()

    for i in mk_list:
        Mk_value = m // i
        Mk_list.append(Mk_value)

    for i in range(n):
        y_list.append(multiplicativeInverse(Mk_list[i], mk_list[i]))

    X = 0
    for i in range(n):
        X += Mk_list[i] * a_list[i] * y_list[i]
    X = X % m
    result = [X]
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
    a = pow(a, 1, m)
    for x in range(1, m):
        if modExp(a * x, 1, m) == 1:
            return x
    return 1


def test(key, X):
    return (modExp(X, 1, key[1])) == key[0]


def main():
    # n = int(input("Choose the number of Generals (n)>>> "))
    n = 5
    result = ChineseRemainderTheoremSetup(n)
    print(result)
    key = result[1]
    print(test(key, result[0]))
    print(test([134, 242], result[0]))

if __name__ == '__main__':
    main()
