def nFirstPrimes1(givenNumber):
    # Initialize a list
    primes = []
    for possiblePrime in range(2, givenNumber + 1):
        # Assume number is prime until shown it is not. 
        isPrime = True
        for num in range(2, possiblePrime):
            if possiblePrime % num == 0:
                isPrime = False
        if isPrime:
            primes.append(possiblePrime)
    return(primes)
  
def nFirstPrimes2(givenNumber):
    # Initialize a list
    primes = []
    for possiblePrime in range(2, givenNumber + 1):
        # Assume number is prime until shown it is not. 
        isPrime = True
        for num in range(2, possiblePrime):
            if possiblePrime % num == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(possiblePrime)
    
   return(primes)
   
   
   def nFirstPrimes3(givenNumber):  
    
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
    
    return(primes)
    
    
    
    
 import timeit
# Approach 1: Execution time 
print(timeit.timeit('nFirstPrimes1(500)', globals=globals(), number=10000))
# Approach 2: Execution time
print(timeit.timeit('nFirstPrimes2(500)', globals=globals(), number=10000))
# Approach 3: Execution time
print(timeit.timeit('nFirstPrimes3(500)', globals=globals(), number=10000))
