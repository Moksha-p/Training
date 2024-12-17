def gen_n_primes(n):
    primes = []
    num = 2
    while len(primes) < n:
        if all(num % i for i in range(2, int(num**0.5) + 1)):
            primes.append(num)
        num += 1
    return primes

if __name__ == '__main__':
    n = 5
    print(f"First {n} prime numbers are:")
    print(gen_n_primes(n))
        
            
