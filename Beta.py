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
    gcd = inverseModN[0]
    if gcd == 1:
        if inverseModN[1] < 0:
            return inverseModN[1] + m
        else:
            return inverseModN[1]
    else:
        #print('No multiplicative inverse for ', str(a), 'mod', str(m))
        return False
      

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

        bigM = getM(Generated_co_primes)
        toBeRemoved = []
        for cP in Generated_co_primes:
            Mi = int(bigM // cP)
            if int(inverseModuleN(Mi, cP)) == False:
                toBeRemoved.append(cP)

        for e in toBeRemoved:
            Generated_co_primes.remove(e)


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
    coCrimesDepth = 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
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
    keyList = []
    for coPrime in co_primes:
        a = get_a(coPrime)
        Mi = int(all_M_multiplied // coPrime)
        x += a * Mi * int(inverseModuleN(Mi, coPrime))
        keyList.append((a, coPrime))
        # print(int(multiplicativeInverse(Mi, coPrime)))
        # print(int(inverseModuleN(Mi, coPrime)))
        #MList.append(Mi)
        #print(r, Mi, Mi % coPrime, X)
        # print(a, 'mod',coPrime , '|', a, Mi, multiplicativeInverse(Mi, coPrime))
        #print(a, 'mod', coPrime)
    #print('x = ', x % all_M_multiplied)
    return [x, co_primes, keyList]


    '''
    x = 30282329560514739880937523243545265002227948803408033760458273597819622259292231078763736643939378064237369129800694074213948946853798334951599563272369652275492744345919994892448947481506740892224970186009627264150519045462851645031849113729047952147524276090715180495108083033210537920185120627876374619402460919322619104903151511172866841674537074492685148583407506025325954704327890853544275148531303980622995982242451066360917954531966923161095569999199285760782819786090359275952132189751559520933021541988979714710312006961292783571096977879605633227228448335928764811526055260449765791060786451513389070353265819925094027714180137686417593516806835448445504253384957506765696832921541254408971458728263829
    
    mms = [
    [208191905539600687785759707066579476111900162934424647660458624952231948471759285841989063606604284601177489269457925423120733137776523813, 36834932695502014155945179750466012709213535211929088206000422368612833513627496585365048030041695112484446128406748851038305401660416564585592],
    [6180937344388701925864482752662736620407569304086841149842924959510794418389277725637893053016895233025549202624879127133127846378814218450277 , 9562794011469004833768051170182814790062994179049317513366691445181014896757819098738525714334814994326626959866429164980503645622780444018031],
    [13522219188102766510891481153183874233809461522377212854903780670686146814399876657373977408535858850523859042008487244835007617168435004682315 , 33544932742438971693926581944161237522160028342583597547870024444391138001315469347654455686108418324426181394465361443918949279857443244514517],
    [3638104994987853369789722273146473615077455121383418886112465854376786987989014812901215109868224484402619178197607573618620768865871521950454 , 92075277877648324979693574256590913401524277872517058067734541874389092811616239697963842275902939988387522472200080453467981139507584367440627],
    [12888883132836226499551183408117094593218024381939035880479713773957086288385909290688584343199025930969726097944423606709517130805402525059334 , 98330868131756652578501588066955603858448377734430244209768077908277960078687942640873883063104002849732184649762725596069382656393904569568545]]
    
    
    for e in mms:
        print(x % e[1] == e[0])    
    '''



    #---------------------myTestingArea-----------------------------

    '''    
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
    '''
def checkSuppliedKeys(x, MList, anonymous_keys, k): # k = threshold
    print(x)
    print(anonymous_keys)
    keysSet = set(anonymous_keys)

    for key in keysSet:
        print((x % key[1]) == key[0])
        
    print(len(keysSet))

    '''
    First users will provide keysList to the system, the keyList will be tested whehter they are valid or fake keys
    if the number validKeys is equal to k then the missile will be launched, 
    otherwise, it will NOT be launched

    in order to prevent the user from supplying the key more than one time, we put the keys into a set

    complexity of brute-force would be 



    '''


    return x


def main():
    #CRT_Setup(5)

    k = 3 #threshold
    x, MList, keys = CRT_Setup(5)
    checkSuppliedKeys(x, MList, keys, k)

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
