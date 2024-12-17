def gen_primes(start, end):
    primes = []
    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                primes.append(num)
    return primes

if __name__ == '__main__':
    s = 10
    e = 30
    print(f"Prime Numbers between {s} and {e} :")
    print(gen_primes(s, e))

