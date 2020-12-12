from MLS import *
import sys, math

sys.setrecursionlimit(4500)


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


# print('coprimeList', generateCoPrime(randomPair)[random.randint(0, 2)])


# print(keys, mList)


# print('N: ', N)
# print(testingKeys)
# print('This is it  ', getXmodM_crt(testingKeys))
# save_keys(testingKeys)


def main():
    print("\n------------------------Setup The System------------------------\n")
    # nDigits_ofN = int(input('How many digits is N?  '))
    k = int(input('What is the threshold (k)? '))  # threshold
    n = int(input('Enter the number of generals (n): '))  # number of keys to be generated
    print("\n------------------------Staff Only------------------------")
    # x, MList, keys = CRT_Setup(n, min_digits)
    # nKeysDigits = nDigits_ofN // 2
    # nKeysDigits = nDigits_ofN // k

    # N = getRandom(nDigits_ofN)  # random
    N = int(input("N>>"))

    Min = 2
    print(Min)
    mList = list()
    M = 1
    keys = []
    while N >= M or (0 in keys):
        keys = []
        M = 1
        mList = list(generatePairWiseCoPrimes(n, math.ceil(pow(N, 1 / k)), math.ceil(pow(N, 1 / (n - k)))))
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
