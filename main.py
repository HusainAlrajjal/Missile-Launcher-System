from MLS import *
import sys
sys.setrecursionlimit(4500)


def generatePairWiseCoPrimes(n, nDigits):
    temp = set()
    count_coPrimes = 0
    temp.add(random.randint(10 ** (nDigits - 1) , (10 ** nDigits) - 1)) # adding some random number to be the first element in the pairwise set
    
    while len(temp) < n:
        r = random.randint(10 ** (nDigits - 1), (10 ** nDigits) - 1)
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

n_equations = 5
nDigits_ofN = 8 # random
nKeysDigits = nDigits_ofN // 2

# print('coprimeList', generateCoPrime(randomPair)[random.randint(0, 2)])

N = getRandom(nDigits_ofN)


mList = list(generatePairWiseCoPrimes(n_equations, nKeysDigits))


keys = [N % m for m in mList]
testingKeys = []

for i in range(len(mList)):
    testingKeys.append((keys[i], mList[i]))

# print(keys, mList)
print('N: ', N)
print(testingKeys)
print('This is it  ', getXmodM_crt(testingKeys))
save_keys(testingKeys)

# print("\n------------------------Setup The System------------------------\n")
# min_digits = int(input('Enter Min digits: '))
# k = int(input('Enter threshold (k): '))            # threshold
# n = int(input('Enter the number of generals (n): '))  # number of keys to be generated

# print("\n------------------------Staff Only------------------------")
# #x, MList, keys = CRT_Setup(n, min_digits)
# N = getRandom(min_digits)
# keys = new_CRT(N, n, min_digits, k)
# print("TOP secret (N)\t\t:", N)
# print("TOP secret length (N)\t\t:", len(str(N)) ," digits")
# # print("TOP secret mods (m_list)\t:", MList)
# # print("Generated Key pairs\t\t\t:", keys)
# print('Condition to succeed (k)\t:', k)
# # print('Validation Result?\t\t\t:', checkSuppliedKeys(x, MList, keys, k))
# print("------------------------Staff Only------------------------\n\n")

# testingKeys = []
# save_keys(keys)
# print("please enter the key pair seperated by space [e.g. 62 102]: ")
# print('To exit, please enter e\n')
# print('k = ', k, 'n = ', n, "\n")
# count = 0
# while True:
#     testingKeys = []
#     count = 0
#     print('*************************** Try again ***************************')
#     while True:
#         count += 1
#         userInput = input("key " + str(count) + ":\t").split()
#         if userInput[0] == 'e' or userInput[1] == 'e':
#             print('')
#             break
#         testingKeys.append((int(userInput[0]), int(userInput[1])))

#     XmodM = getXmodM_crt(set(testingKeys))
#     print('test2: ', XmodM )

#     x = XmodM[0]
#     M = XmodM[1]

#     print(x, N)
#     if x == N and len(testingKeys) <= k:
#         print('Welcome!, you may launch the Missile to destroy anything you want 😈\n')
#     else:
#         print('You are not allowed to launch the Missile, Please Stop Hacking Our System!😉')
