


# Write a Python program to find all the prime numbers between two given numbers.
def primes(start, end):
    prime = []
    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    break
            else:
                prime.append(num)
    return prime

start = int(input('Enter start: '))
end = int(input('Enter end: '))
print('The prime numbers in the range are: ',primes(start, end))

#Write a Python program to find the first n numbers that are both prime.

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
def primes(n):
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

n = 10
result = primes(n)
print(result)

#Write a Python function to find the longest word in a given sentence
def longestWord(s):
    words = s.split()
    longest_word = max(words, key=len)
    return longest_word
s = input('Enter a sentence: ')
print('The longest word is:', longestWord(s))

#Write a Python function to check if two given strings are anagrams of each other
def anagrams(s1,s2):
    if sorted(s1)== sorted(s2):
        print('anagrams')
        return True
    else:
        print('not anagrams')
        return False
    return False
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
anagrams(s1,s2)

#Create a program that evaluates a list of Boolean expressions and returns the count of True values.
def countTrue(expressions):
    return sum(1 for expression in expressions if eval(expression))

expressions = ["True", "False", "True", "True", "False","True"]
print(countTrue(expressions))

#Write a Python function to evaluate a complex Boolean expression represented as a string
s= input('Enter expression')
eval(s)

#Write a Python function to find the second largest element in a list.
def secondLargest(lists):
    a = 0
    b= 0
    for i in lists:
        if i>a:
            b=a
            a=i
        elif i>b:
            b= i
    return b

lst = [10, 20, 30, 40, 50]
print(secondLargest(lst))

#Write a Python program to generate all possible permutations of a list of numbers.
import itertools
def genPerm(lst):
    return list(itertools.permutations(lst))

lst = [1,2,3]
print(genPerm(lst))

#Create a function to merge two sorted tuples into one sorted tuple.
def mergeTuples(t1,t2):
   return tuple(sorted(t1+t2))
t1 = (1,4,2,5,8)
t2 = (3,6,7,9,0)
print(mergeTuples(tuple1, tuple2))

#Write a Python program to find all unique combinations of elements in a tuple that sum up to a given number.


def tuples(elements, target):
    result = set()
    n = len(elements)

    for r in range(1, n + 1):
        for combo in combinations(elements, r):
            if sum(combo) == target:
                result.add(tuple(sorted(combo)))

    return list(result)



tuple1 = (2, 3, 5, 7)

t = 10
tup = tuples(tuple1,t)
for i in tup:
    print(i)

#Write a Python function to invert a dictionary, swapping keys and values
def invert(d):
    return {v: k for k, v in d.items()}

d = {'a': 1,
'b': 2,
'c': 3}
print(invert(d))

#Write a Python program to merge multiple dictionaries and sum the values of common keys
def mergeDicts(*dicts):
    result = {}
    for d in dicts:
        for k, v in d.items():
            if k in result:
                result[k] += v
            else:
                result[k] = v
    return result
d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'c': 4}
print(mergeDicts(d1,d2))

#Write a Python program to find the symmetric difference between two sets.
def symmetricDifference(set1, set2):
    return set1.symmetric_difference(set2)
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(symmetricDifference(set1,set2))

#Write a Python function to find all subsets of a given set.
def findSubsets(s):
    subsets = [[]]
    for elem in s:
        subsets += [subset + [elem] for subset in subsets]
    return subsets

s = {1, 2, 3}
print(findSubsets(s))

#Write a Python program to classify a given year as a leap year or a non-leap year.
def leapYear(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print('Leap Year')
        return True
    print('Not Leap year')
    return False
year = int(input('Enter Year'))
print(leapYear(year))

#Write a Python program to solve a quadratic equation (ax^2 + bx + c = 0) and classify the roots as real, complex, or equal

def quadraticRoots(a,b,c):
    d = (b**2)-(4*a*c)
    r1 = ((-b)+ (d**0.5))/(2*a)
    r2 = ((-b)- (d**0.5))/(2*a)
    return r1,r2

a=1
b=-3
c=2
roots = quadraticRoots(a, b, c)
print(f"The roots are: {roots[0]} and {roots[1]}")

#Write a Python function to generate the Fibonacci series up to a given number of terms
def fibonacci(n):

    if n <= 0:
        return "Please enter a positive integer."
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < n:
        next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_term)
    return fibonacci_sequence[:n]


num_terms = 10
print(fibonacci(num_terms))

#Write a Python program to find the longest increasing subsequence in a given list of numbers

def longestIncSubseq(nums):
    if not nums:
        return []

    lis = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                lis[i] = max(lis[i], lis[j] + 1)

    max_len = max(lis)
    result = []
    for i in range(len(nums) - 1, -1, -1):
        if lis[i] == max_len:
            result.append(nums[i])
            max_len -= 1

    return result[::-1]

nums = [10, 22, 9, 33, 21, 50, 41, 60, 80]
print(longestIncSubseq(nums))

#Write a Python program to find the greatest common divisor (GCD) of two numbers using the Euclidean algorithm
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

a = int(input("Enter first num: "))
b = int(input("Enter second num: "))
result = gcd(a, b)
print(f"The GCD of {a} and {b} is: {result}")

#Write a Python program to implement a basic version of the Collatz conjecture.

def collatz(n):
    if n <= 0:
        return "The number is not positive"
    list = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n  = 3 * n + 1
        list.append(n)
    return list
c = int(input('Enter number'))
collatz(c)

