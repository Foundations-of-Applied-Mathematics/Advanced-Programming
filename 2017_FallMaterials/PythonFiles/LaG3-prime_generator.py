import time

def generate_primes1(n):
    """Returns a list of Primes where each prime is <= n"""
    start = time.time()
    primes = []
    for i in range(2,n+1):
        potential_prime = True
        for j in range(2,i):
            if i % j == 0:
                #print("The number", i, "is evenly div. by:", j)
                potential_prime = False
                break
        if potential_prime is True:
            primes.append(i)
    print(time.time() - start, "Seconds elapsed for primes up to", n)
    return primes

def generate_primes2(n):
    """Returns a list of primes where each prime is <= n"""
    start = time.time()
    primes = [2]
    for i in range(3,n+1,2):
        potential_prime = True
        for j in range(2,i):
            if i % j == 0:
                #print("The number", i, "is evenly div. by:", j)
                potential_prime = False
                break
        if potential_prime is True:
            primes.append(i)
    print(time.time() - start, "Seconds elapsed for primes up to", n)
    return primes

def generate_primes3(n):
    """Returns a list of primes where each prime is <= n"""
    start = time.time()
    primes = []
    for i in range(2,n+1):
        potential_prime = True
        for j in range(2,round(i**0.5)+1):
            if i % j == 0:
                #print("The number", i, "is evenly div. by:", j)
                potential_prime = False
                break
        if potential_prime is True:
            primes.append(i)
    print(time.time() - start, "Seconds elapsed for primes up to", n)
    return primes

## Code taken from a Stack Overflow for generating these primes
def generate_primes4(n):
    start = time.time()
    primes = set()
    def isPrime(x):
      if x in primes:
        return x
      for i in primes:
        if not x % i:
          return None
      else:
        primes.add(x)
        return x

    myfil = filter(isPrime, range(2,n))
    for i in myfil:
        C = 1 + 1
    print(time.time() - start, "seconds elapsed for primes up to", n)

def generate_n_primes(n):
    """This function generates the first n prime numbers"""
    primes = []

def test_prime_generator(func, N=500001, stepsize=50000):
    for n in range(50000, N, stepsize):
        plist2 = func(n) #takes about 0.0555 seconds

def validate_two_lists(f1, f2, n):
    """Accept two prime generators as functions that take an argument n for each function"""
    return f1(n) == f2(n)

def generate_pfs(n):
    """Given a positive integer n, returns its prime factors"""
    factors = []
    i = 2
    while i**2 <= n:
        if n % i == 0:
            factors.append(i)
            n //= i
        else:
            i += 1
    if n > 1:
        factors.append(n)
    print(factors)
