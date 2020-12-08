import random
import time

def gcd(a, b):
    if b == 0:
        return a
    elif a >= b:
        return gcd(b, pow(a, 1, b))
    else:
        return gcd(b, a)


def EEA(a, b):
    # Base source https://www.geeksforgeeks.org/python-program-for-basic-and-extended-euclidean-algorithms-2/
    # Base Case
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = EEA(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y


def inverseModuleN(a, m):
    inverseModN = EEA(a, m)
    gcd = inverseModN[0]
    if gcd == 1:
        if inverseModN[1] < 0:
            return inverseModN[1] + m
        else:
            return inverseModN[1]
    else:
        '''
        'No multiplicative inverse for ', str(a), 'mod', str(m))
        '''
        return False


def test(key, X, mlist):
    for i in mlist:
        if key[1] == i and key[1] != 0:
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


# generate pwList from start up to end inclusive
def pwListGenerator(start, end):
    if start < end:
        end += 1
        pwList = open("keys.txt", "w")
        for i in range(start, end):  # 99999
            for j in range(start, end):
                r = [i, j]
                pwList.write(str(i) + "\t" + str(j) + "\n")
        pwList.close()


def bruteForce(pwList):
    # pwListGenerator(10000, 14000)
    attackKeys = []
    with open(pwList, 'r') as keys:
        for line in keys:
            attackKeys.append([int(line.split()[0]), int(line.split()[1])])
        keys.close()
    return attackKeys


# masqurading
def Hbrute_force(N):
    pairs = list()
    N = 10 ** N
    for n in range(2, N):
        for i in range(1, n):
            pairs.append((i, n))
            print((i, n))
    return pairs, len(pairs)


def generateCoPrime(list):
    '''
        All pairs of positive coprime numbers ( m , n ) (with m > n ) can be arranged in two disjoint complete ternary trees, one tree starting from ( 2 , 1 ) 
        (for even-odd and odd-even pairs), and the other tree starting from ( 3 , 1 )(for odd-odd pairs).
        The children of each vertex ( m , n ) are generated as follows:

            Branch 1: ( 2 m − n , m )
            Branch 2: ( 2 m + n , m )
            Branch 3: ( m + 2 n , n )

        This scheme is exhaustive and non-redundant with no invalid members. 
    '''
    m, n = list

    if gcd(m, n) == 1:
        if m > n:
            pair1 = [2 * m - n, m]
            pair2 = [2 * m + n, m]
            pair3 = [m + 2 * n, n]
        else:
            pair1 = [2 * n - m, n]
            pair2 = [2 * n + m, n]
            pair3 = [n + 2 * m, m]
    else:
        return -1
    return pair1, pair2, pair3


def getRandomCoPrimePair(n):  # n is the maximum of the random number
    '''
    This function returns a pair of random co-prime numbers between 2 and n
    '''

    if n == 2:  # Fixes unresponding problem
        n += 1
    r = []
    while True:
        r = [random.randint(2, n), random.randint(2, n)]
        # print(r)
        if gcd(r[0], r[1]) == 1:
            return r


def randomCoPrimePair(min_digits, max_digits):  # n is the maximum of the random number
    '''
    This function returns a pair of random co-prime numbers between 2 and n
    '''
    r = []
    while True:
        r = [random.randint(10 ** (min_digits - 1), 10 ** (max_digits -1 )), random.randint(10 ** (min_digits - 1), 10 ** (max_digits - 1))]
        # print(r)
        if gcd(r[0], r[1]) == 1:
            return r



def getCoPrimes(n_equations, depthOfRandomness):
    Random_co_primes = []
    Generated_co_primes = set()
    while len(Generated_co_primes) < n_equations:

        # ------------------------- generating co_primes block ---------------------
        someRandom = random.randint(2, depthOfRandomness)
        g = generateCoPrime(getRandomCoPrimePair(someRandom))[
            random.randint(0, 2)]
        Generated_co_primes.add(g[0])
        Generated_co_primes.add(g[1])
        # ----------------------------------block end ------------------------------

        bigM = getM(Generated_co_primes)
        toBeRemoved = []
        for cP in Generated_co_primes:
            Mi = int(bigM // cP)
            if int(inverseModuleN(Mi, cP)) == False:
                toBeRemoved.append(cP)

        for e in toBeRemoved:
            Generated_co_primes.remove(e)

    if len(Generated_co_primes) == (n_equations + 1):
        Generated_co_primes.pop()
    return Generated_co_primes


def getM(mList):
    M = 1
    for m in mList:
        M *= m
    return M


def get_a(m):
    while True:
        r = random.randint(2, m)
        if gcd(r, m) == 1 and r != m:
            return r


def CRT_Setup(n_equations, min_digits):
    coPrimesDepth = 10 ** min_digits
    co_primes = getCoPrimes(n_equations, coPrimesDepth)
    # ---------------------myTestingArea-----------------------------

    all_M_multiplied = getM(co_primes)
    x = 0
    keyList = []
    for coPrime in co_primes:
        a = get_a(coPrime)
        Mi = int(all_M_multiplied // coPrime)
        x += a * Mi * int(inverseModuleN(Mi, coPrime))
        keyList.append((a, coPrime))

    # hashedKeys = createHashedKeys(keyList)
    # keyList = [(2, 3), (3, 5), (2, 7)]
    # print(getXmodM_crt(keyList))
    return [x % all_M_multiplied, co_primes, keyList]

    # ---------------------myTestingArea-----------------------------
def getXmodM_crt(keys):
    '''
    syntax keyList = [(2, 3), (3, 5), (2, 7)]
    '''
    tempXmodM = []
    all_M_multiplied = 1
    x = 0
    #print(keys, '////////////////////////')
    for k in keys:
        all_M_multiplied *= k[1]  # multiplying all M to get BigM
    for key in keys:
        Mi = int(all_M_multiplied // key[1])
        x += key[0] * Mi * int(inverseModuleN(Mi, key[1]))

    #print(x % all_M_multiplied, all_M_multiplied, '---------------')
    return x % all_M_multiplied, all_M_multiplied


def nCr(pair_list, r, n):
    pair_list = set(pair_list)
    comb = list()
    for i in range(r, n + 1):
        comb += combinations(pair_list, i)
    return list(comb)

def allCoPrimes(lengthOfCoPrimeList, start_randomPair):
    coprimes = set()
    pair = generateCoPrime(randomPair)[random.randint(0, 2)]
    coprimes.add(pair[0], [1])

    while len(coprimes) < lengthOfCoPrimeList:
        tempPair = generateCoPrime(pair)[random.randint(0, 2)]
        coprimes.add(tempPair[0])
        coprimes.add(tempPair[1])
    return coprimes
 
def new_CRT(N, n_equations, min_digits, threshold_k):
    # 1- Generate N
    # 2- Generate m list
    coPrimesDepth = len(str(N)) // (n_equations - 4)
    # PairPrime = getXXXXX(coPrimesDepth, min_digits)
    # coPPs = generateCoPrime(PairPrime)[0]
    # for e in coPPs:
    #     c = getCoPrime(e)
    #     print(c)
    # print(coPPs)
    # print('-------------------------')
    # for p in PairPrime:
    #     print(len(str(p)))
    # print('-------------------------')

    co_primes = getCoPrimes(n_equations, 10 ** min_digits)
    randomPair = randomCoPrimePair(min_digits, int(min_digits * 1.30))
    print('randomCoPrimes: ', randomPair)
    print('coprimeList', generateCoPrime(randomPair)[random.randint(0, 2)])
    key_list = set()
    # 3- Key_list
    all_M_multiplied = 1
    for coPrime in co_primes:
        key_list.add(((N % coPrime), coPrime))
        all_M_multiplied *= coPrime
    # 4- Key Testing CRT(keylist)
    #tested = getXmodM_crt(key_list)
    #print("new CRT")
    print(co_primes)
    print(N, len(str(N)))
    print(all_M_multiplied, len(str(all_M_multiplied)))
    #print("NewCRT")
    return key_list


def checkSuppliedKeys(x, MList, anonymous_keys, k):  # k = threshold
    if k <= 2:
        return False
    else:
        if len(MList) < k:
            return False, 'The missile needs at least ' + str(k) + ' keys to launch it but only ' + str(
                len(MList)) + ' were generated 😂😂'

        keysSet = set(anonymous_keys)
        if len(keysSet) < k:
            return False, 'No sufficient keys were provided!!😢'

        true_test = 0
        for key in keysSet:
            if test(key, x, MList):
                true_test += 1

        if true_test < k:
            return False, 'You are not allowed to launch the Missile, Please Stop Hacking Our System!😉'
        return k <= true_test
