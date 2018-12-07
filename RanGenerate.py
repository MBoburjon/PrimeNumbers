import math
from datetime import datetime
from random import *

def SieveAlgorithm():
    num = 200
    Mylist = [True] * num
    result = []

    for x in range(2, int(math.sqrt(num))):
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

        checkList = SieveAlgorithm()
        for x in checkList:
            if num % x == 0 and num != x:
                return False
        for x in range(199, int(math.sqrt(num))):
            if num % x == 0:
                return False

    return True
def GenerateNums(num, NumLength):
    """Starting = 1 * pow(10, (num - 1))

    EndLimit = pow(10, num) - 1
    RanList = []
    RanPrimes = []
    count = 0

    for x in range(Starting, EndLimit):
        RanList.append(x)
    #while count <= NumLength:

    for x in RanList:
        if PrimalityTest(x):
            RanPrimes.append(x)
            print(x)
    """
    result = False
    RanNumber = 0
    while result != True:
        RanNumber = randint((pow(10, (num - 1))), ((pow(10, num))-1))
        if PrimalityTest(RanNumber):
            result = True

    return RanNumber



#start = timeit.default_timer()

start = datetime.now()

num = int(input("Enter num of digit to generate prime num:"))
print(num)
NumLength = int(input("Enter number of primes you want: "))
print(NumLength)

number = 2074722246773485207821695222107608587480996474721117292752992589912196684750549658310084416732550077
number2 = 7931271602685361144914564178565893280443229361157745990678453548168166804156619919047317995514821091
print(PrimalityTest(number))
#print(GenerateNums(num, NumLength))

#stop = timeit.default_timer()
print("Time: ", datetime.now() - start)

