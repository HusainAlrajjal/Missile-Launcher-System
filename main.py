from MLS import *
import sys
sys.setrecursionlimit(4500)


def save_keys(keys):
    pwList = open("keys.txt", "w")
    for key in keys:  # 99999
        pwList.write(str(key[0]) + "    " + str(key[1]) + "\n")
    pwList.close()



print("\n------------------------Staff Only------------------------")
min_digits = int(input('Enter Min digits>>'))
k = int(input('Enter threshold (k) >>'))            # threshold
n = int(input('Enter the number of generals (n) >>'))   # number of keys to be generated
x, MList, keys = CRT_Setup(n, min_digits)
print("TOP secret (N)\t\t:", x)
print("TOP secret length (N)\t\t:", len(str(x)) ," digits")
# print("TOP secret mods (m_list)\t:", MList)
# print("Generated Key pairs\t\t\t:", keys)
print('Condition to succeed (k)\t:', k)
# print('Validation Result?\t\t\t:', checkSuppliedKeys(x, MList, keys, k))
print("------------------------Staff Only------------------------\n\n")

testingKeys = []
save_keys(keys)
print("please enter the key pair seperated by space [e.g. 62 102]: ")
print('To exit, please enter e\n')
print('k = ', k, 'n = ', n, "\n")
count = 0
while True:
    count += 1
    userInput = input("key " + str(count) + ":\t").split()
    if userInput[0] == 'e' or userInput[1] == 'e':
        print()
        break
    testingKeys.append((int(userInput[0]), int(userInput[1])))


#print(testingKeys)
isAllowed = checkSuppliedKeys(x, MList, testingKeys, k)
if isAllowed == True:
    print('Welcome!, you may launch the Missile to destroy anything you want :)\n')
else:
    print(isAllowed[1], "\n")

# for k in keys:
#     if gcd(k[0], k[1]) != 1:
#         print(k, 'Bug in your system')

'''
Brute Force Attack Testing
ti = time.time_ns()
brute_force_keys = Hbrute_force(digits)
ti = time.time_ns() - ti
print(ti / (1000000000), 'sec')
ti = time.time_ns()
print('Validation Result?\t\t\t:', checkSuppliedKeys(x, MList, brute_force_keys[0], k), brute_force_keys[1])
ti = time.time_ns() - ti
print(ti / (1000000000), 'sec')
'''
# n = int(input("Choose the number of Generals (n)>>> "))
# result = ChineseRemainderTheoremSetup(n)
# print(result)
# result = [2551626037209230983216, [98041, 13691, 42797, 1217, 60601], [79839, 98041], [10112, 13691],
#           [10615, 42797], [1085, 1217], [47146, 60601]]
# SecretKey = result[0]
# mlist = result[1]
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
