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


def EEA(a, b):
    #Base source https://www.geeksforgeeks.org/python-program-for-basic-and-extended-euclidean-algorithms-2/
    # Base Case  
    if a == 0 :   
        return b,0,1
             
    gcd,x1,y1 = EEA(b%a, a)  
     
    # Update x and y using results of recursive  
    # call  
    x = y1 - (b//a) * x1  
    y = x1  
     
    return gcd,x,y 

def inverseModuleN(a, m):
    inverseModN = EEA(a, m)

    if inverseModN[1] < 0:
        return inverseModN[1] + m
    else:
        return inverseModN[1]
      

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

# generate pwList from start up to end inclusive
def pwListGenerator(start, end):
    if start < end:
        end += 1
        pwList = open("keys.txt", "w")
        for i in range(start, end): #99999
            for j in range(start, end):
                r = [i, j]
                pwList.write(str(i) +" "+ str(j) + "\n")
        pwList.close()


def bruteForce(pwList):
    #pwListGenerator(10000, 14000)
    attackKeys = []
    with open(pwList,'r') as keys: 
        for line in keys:
            attackKeys.append([int(line.split()[0]), int(line.split()[1])])
        keys.close()
    return attackKeys

# m > n
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

def getRandomCoPrimePair(n): # n is the maximum of the random number
    if n == 2: # Fixes unresponding problem
        n += 1
    r = []
    while True:
        r = [random.randint(2, n), random.randint(2, n)]
        #print(r)
        if (gcd(r[0], r[1]) == 1):
            return r

def getCoPrimes(n, depthOfRandomness):
    # n += 1
    Random_co_primes = []
    Generated_co_primes = set()
    # for i in range(int(n/2)):
    while len(Generated_co_primes) < n:
        '''
    # random co_primes block
        r = getRandomCoPrimePair(1000)
        Random_co_primes.append(r[0])
        Random_co_primes.append(r[1])
    # block end ------------------
        '''
    # generated co_primes block
        #  g = generateCoPrime(getRandomCoPrimePair(you might specify the max possible mk value from here))[random.randint(0, 2)]
        g = generateCoPrime(getRandomCoPrimePair(random.randint(2, depthOfRandomness)))[random.randint(0, 2)]
        # print(g)
        Generated_co_primes.add(g[0])
        Generated_co_primes.add(g[1])
        #print(len(Generated_co_primes))
    # block end ------------------
    if len(Generated_co_primes) == (n+1):
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

def CRT_Setup(n_equations):

    address = "10000prime.txt"
    primes = import_primes(address)
    coCrimesDepth = 12
    co_primes = getCoPrimes(n_equations, coCrimesDepth)
    #print(co_primes)

    #primes = co_primes
    # choosing a prime randomly from the dataset 1000prime.
    mk_list = list()
    m = 1
    for i in range(n_equations):
        r = random.randint(0, len(primes) - 1)
        mk_list.append(primes[r])
        m *= mk_list[i]
    # choosing a where a is from  a mod mk
    a_list = list()
    i = 0

    #print(mk_list)

    # generate co-prime to mk
    while i < n_equations:
        # problem 1: random number should be >= size(n digits
        r = random.randint(10 ** (len(str(mk_list[i])) - 1), mk_list[i] - 1)
        #
        if gcd(r, mk_list[i]) == 1:
            a_list.append(r)
            i += 1
    # end of generating co-primes of mk

    #---------------------myTestingArea-----------------------------

    all_M_multiplied = getM(co_primes)
    # co_primes = [3, 5, 7]
    # all_M_multiplied = 105
    x = 0
    #print('a', 'mod','m' , '|', 'a',' M', '(M mod coPrime)')
    MList = list()
    for coPrime in co_primes:
        a = get_a(coPrime)
        Mi = int(all_M_multiplied // coPrime)
        x += a * Mi * int(inverseModuleN(Mi, coPrime))
        MList.append(Mi)
        #print(r, Mi, Mi % coPrime, X)
        # print(a, 'mod',coPrime , '|', a, Mi, multiplicativeInverse(Mi, coPrime))
        print(a, 'mod', coPrime)
    print('x = ', x % all_M_multiplied)
    print(len(str(x)))

    for m in MList:
        print(x % m)




    #---------------------myTestingArea-----------------------------

    
    Mk_list = list()
    for i in mk_list:
        Mk_value = m // i
        Mk_list.append(Mk_value)

    y_list = list()
    for i in range(n_equations):
        y_list.append(multiplicativeInverse(Mk_list[i], mk_list[i]))

    X = 0
    # X is 23 and m = 105
    for i in range(n_equations):
        X += Mk_list[i] * a_list[i] * y_list[i]
    X = X % m

    result = [X, mk_list]
    for i in range(n_equations):
        result.append([a_list[i], mk_list[i]])
    return result


def main():
    CRT_Setup(5)
    #print(CRT_Setup(5))
    # n = int(input("Choose the number of Generals (n)>>> "))
    n = 5
    # result = ChineseRemainderTheoremSetup(n)
    # print(result)
    result = [2551626037209230983216, [98041, 13691, 42797, 1217, 60601], [79839, 98041], [10112, 13691],
              [10615, 42797], [1085, 1217], [47146, 60601]]
    SecretKey = result[0]
    mlist = result[1]
'''
    for i in result[2:]:
        print(i, test(i, SecretKey, mlist))
 
    #pwListGenerator(1085, 1300)
    #attackList = genAttack(5, 10000)
    attackList = bruteForce('keys.txt')
    for i in attackList:
        if test(i, SecretKey, mlist):
            print(i, "We have broke your system :)")

    #print(test([79839, 98041], SecretKey, mlist))
'''

if __name__ == '__main__':
    main()
