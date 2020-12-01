from MLS import *
import sys
sys.setrecursionlimit(5000)


min_digits = 2
k = 10 # threshold
n = 10  # number of keys to be generated

x, MList, keys = CRT_Setup(n, min_digits)
print("TOP secret (X)\t\t\t\t:", x)
print("TOP secret length (X)\t\t:", len(str(x)))
print("TOP secret mods (m_list)\t:", MList)
print("Generated Key pairs\t\t\t:", keys)
print('Condition to succeed (k)\t:', k)
print('Validation Result?\t\t\t:', checkSuppliedKeys(x, MList, keys, k))
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