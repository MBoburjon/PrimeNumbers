def approach3(givenNumber):
    # Initialize a list
    primes = []
    for possiblePrime in range(2, givenNumber + 1):

        # Assume number is prime until shown it is not.
        isPrime = True
        for num in range(2, int(possiblePrime ** 0.5) + 1):
            if possiblePrime % num == 0:
                isPrime = False
                break

        if isPrime:
            primes.append(possiblePrime)

    return (primes)


num = pow(10, 10) - 1

result = approach3(num)

for x in num:
    print(x)

