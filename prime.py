num = range(1, 10000)

def prime(num):
      for i in range(2, num):
            if(num%i) == 0:
                  return False
            else:
                  return True
primes = list(filter(prime, num))
print(primes)