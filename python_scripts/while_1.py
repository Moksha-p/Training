def find_gcd(num1, num2):
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    return num1

if __name__ == '__main__':
    num1 = 48
    num2 = 18
    print(f"GCD of {num1} and {num2} is: {find_gcd(num1, num2)}")