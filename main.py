from MLS import *
import sys, math, random

sys.setrecursionlimit(5000)

def nth_root(x, n):
    # Start with some reasonable bounds around the nth root.
    upper_bound = 1
    while upper_bound ** n <= x:
        upper_bound *= 2
    lower_bound = upper_bound // 2
    # Keep searching for a better result as long as the bounds make sense.
    while lower_bound < upper_bound:
        mid = (lower_bound + upper_bound) // 2
        mid_nth = mid ** n
        if lower_bound < mid and mid_nth < x:
            lower_bound = mid
        elif upper_bound > mid and mid_nth > x:
            upper_bound = mid
        else:
            # Found perfect nth root.
            return mid
    return mid + 1

def generatePairWiseCoPrimes(n, Min, Max):
    temp = set()
    count_coPrimes = 0
    temp.add(random.randint(Min, Max))  # adding some random number to be the first element in the pairwise set

    while len(temp) < n:
        r = random.randint(Min, Max)
        for e in temp:
            #  print(e, r, gcd(e, r))
            if gcd(e, r) == 1:
                count_coPrimes += 1
            else:
                break
        if count_coPrimes == len(temp):
            temp.add(r)
        count_coPrimes = 0
    #  print('----------------------')
    return temp


def save_keys(keys):
    pwList = open("keys.txt", "w")
    for key in keys:  # 99999
        pwList.write(str(key[0]) + "    " + str(key[1]) + "\n")
    pwList.close()


def main():
    print("\n------------------------Setup The System------------------------\n")
    k = int(input('What is the threshold (k)? '))  # threshold
    n = int(input('Enter the number of generals (n): '))  # number of keys to be generated
    if n < k:
        print('INPUT ERROR: k cannot be greater than n')
        main() 
    print("\n------------------------Staff Only------------------------")

    N = int(input("N>>"))

    mList = list()
    M = 1
    keys = []
    minimum, maximum = math.ceil(nth_root(N, k)), math.floor(nth_root(N, k-1))

    print('minimum: ', minimum, ' maximum: ', maximum)
    range_possible = maximum - minimum + 1
    if (k ** 2) > range_possible:
        val_list = list(range(minimum, maximum + 1))
        n_cop = restircted_max_coprime(n, val_list)
        if range_possible < n or n_cop < n:
            print('It is not feasible!!')
            return

    while N >= M or (0 in keys):
        keys = []
        M = 1
        mList = list(generatePairWiseCoPrimes(n, minimum, maximum))
        for m in mList:
            M *= m
        keys = [N % m for m in mList]

    # keys = new_CRT(N, n, min_digits, k)
    print("TOP secret (N)\t\t:", N)
    print("TOP secret length (N)\t\t:", len(str(N)), " digits")
    print("TOP secret mods (m_list)\t:", mList)
    print("Generated Key pairs\t\t\t:", keys)
    print('Condition to succeed (k)\t:', k)
    # print('Validation Result?\t\t\t:', checkSuppliedKeys(x, MList, keys, k))
    print("------------------------Staff Only------------------------\n\n")

    testingKeys = []
    for i in range(len(mList)):
        testingKeys.append((keys[i], mList[i]))
    save_keys(testingKeys)

    print("please enter the key pair seperated by space [e.g. 62 102]: ")
    print('To exit, please enter e\n')
    print('k = ', k, 'n = ', n, "\n")
    count = 0
    while True:
        testingKeys = []
        count = 0
        print('*************************** Try again ***************************')
        while True:
            count += 1
            userInput = input("key " + str(count) + ":\t").split()
            if userInput[0] == 'e' or userInput[1] == 'e':
                print('')
                break
            testingKeys.append((int(userInput[0]), int(userInput[1])))

        XmodM = getXmodM_crt(set(testingKeys))

        x = XmodM[0]
        M = XmodM[1]

        print(x, N)
        if x == N and len(testingKeys) >= k:
            print('Welcome!, you may launch the Missile to destroy anything you want 😈\n')
        else:
            print('You are not allowed to launch the Missile, Please Stop Hacking Our System!😉')


if __name__ == '__main__':
    main()
