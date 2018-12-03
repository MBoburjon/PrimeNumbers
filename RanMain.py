import math
from datetime import datetime

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

    return True
def JohnSelfridge(num):

    result = math.pow(2, (num - 1))

    print(result)
    print((result % num))
    if (result % num) == 1:
        return True
    else:
        return False




#start = timeit.default_timer()

start = datetime.now()

num = int(input("Enter num to check for primality:"))
print(num)
print(PrimalityTest(num))

#stop = timeit.default_timer()
print("Time: ", datetime.now() - start)

