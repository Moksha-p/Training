# 1. Numbers - Write a Python program to find all the prime numbers between two given numbers.
print('Write a Python program to find all the prime numbers between two given numbers.')

def find_prime_numbers(start, end):
    prime_numbers = []
    for num in range(start, end + 1):
        if num > 1: 
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:  
                    break
            else:
                prime_numbers.append(num)
    return prime_numbers  

# Example usage
start = int(input('Enter the starting number: '))
end = int(input('Enter the ending number: '))
print('The prime numbers in the range are: ',find_prime_numbers(start, end))

