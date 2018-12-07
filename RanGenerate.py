import math
from datetime import datetime
from random import *

def SieveAlgorithm(num):

    Mylist = [True] * num
    result = []

    for x in range(2, num):
        if Mylist[x] == True:
            y = pow(x, 2)
            count = 1
            while y < num:
                Mylist[y] = False
                y = y + (x * count)

    for j in range(2, len(Mylist)):
        if Mylist[j] == True:
            result.append(j)

    return result


def PrimalityTest(num):
    result = False

    if num <= 3:
        return num > 1
    elif num % 2 == 0 or num % 3 == 0:
        return False
    else:

        checkList = SieveAlgorithm(200)
        for x in checkList:
            if num % x == 0 and num != x:
                return False

        loop = 5

        while (loop * loop) <= num:
            if (num % loop) == 0 or (num % (loop + 2)) == 0:
                return False
            loop = loop + 6

    return True

def GenerateNums(num):

    if num <= 20:
        result = False

        RanNumber = 0
        while result != True:
            RanNumber = randint((pow(10, (num - 1))), ((pow(10, num)) - 1))
            if PrimalityTest(RanNumber):
                result = True

        return RanNumber

    else:
        print("hi man")



#start = timeit.default_timer()

start = datetime.now()

num = int(input("Enter num of digit to generate prime num:"))
print(num)

NumLength = int(input("Enter number of primes you want: "))
print(NumLength)



for x in range(0, NumLength):
    print(GenerateNums(num))



print("Time: ", datetime.now() - start)

