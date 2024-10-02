#prime number or not
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))
primes_in_range = find_primes(start, end)
print(f"Prime numbers between {start} and {end}: {primes_in_range}")


# WriteaPython program to find the first n numbers that are both prime.
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def first_n_primes(n):
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

n = int(input("Enter the number of primes to find: "))
primes = first_n_primes(n)
print(f"The first {n} prime numbers are: {primes}")





