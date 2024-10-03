import itertools
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

# 2. Write a Python program to find the first n numbers that are both prime.
print('Write a Python program to find the first n numbers that are both prime.')
def is_prime(num):
    if num <= 1:
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


n = int(input("Enter the value of n: "))
result = first_n_primes(n)   
print('The first {n} primes are :', result) 

# 3. Write a Python function to find the longest word in a given sentence.
print('Write a Python function to find the longest word in a given sentence.')
def find_longest_word(sentence):
    words = sentence.split()
    longest_word = max(words, key=len)
    return longest_word
    sentence = input('Enter a sentence: ')
    print('The longest word is:', find_longest_word(sentence))

sentence = input(' Enter your sentence here : ')
print('Sentence is :',sentence)
print('The longest word is:', find_longest_word(sentence))

# 4. Write a Python function to check if two given strings are anagrams of each other.
print('Write a Python function to check if two given strings are anagrams of each other.')
def are_anagrams(str1, str2):
    if len(str1) != len(str2):
        print(f"'{str1}' and '{str2}' are not anagrams.")
        return False
    return print(f"'{str1}' and '{str2}' are anagrams.",sorted(str1) == sorted(str2))
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

are_anagrams(str1, str2)


# 5. Create a program that evaluates a list of Boolean expressions and returns the count of True values.
print('Create a program that evaluates a list of Boolean expressions and returns the count of True values.')

def count_true_expressions(expressions):
    return sum(1 for expression in expressions if eval(expression))

expressions = ["True", "False", "True", "True", "False","True"]
print(count_true_expressions(expressions))

# 6. Write a Python function to evaluate a complex Boolean expression represented as a string
print('Write a Python function to evaluate a complex Boolean expression represented as a string.')

def evaluate_expression(expression):
    return eval(expression)

expression = input("Enter the expression: ")
print(evaluate_expression(expression))

# 7. Write a Python function to find the second largest element in a list.
print('Write a Python function to find the second largest element in a list.')
def find_second_largest(lst):
    if len(lst) < 2:
        return None
    return sorted(lst)[-2]

lst = [10, 20, 30, 40, 50]
print(find_second_largest(lst))

# 8. Write a Python program to generate all possible permutations of a list of numbers.
print('Write a Python program to generate all possible permutations of a list of numbers.')

def generate_permutations(lst):
    return list(itertools.permutations(lst))

lst = [1,2,3]
print(generate_permutations(lst))

# 9. Create a function to merge two sorted tuples into one sorted tuple.
print('Create a function to merge two sorted tuples into one sorted tuple.')
def merge_sorted_tuples(tuple1, tuple2):
    return tuple(sorted(tuple1 + tuple2))

tuple1 = (1,4,2,5,8)
tuple2 = (3,6,7,9,0)
print(merge_sorted_tuples(tuple1, tuple2))

# 10. Write a Python program to find all unique combinations of elements in a tuple that sum up to a given number.
print('Write a Python program to find all unique combinations of elements in a tuple that sum up to a given number.')

# 11. Write a Python function to invert a dictionary, swapping keys and values.
print('Write a Python function to invert a dictionary, swapping keys and values.')
def invert_dict(d):
    return {v: k for k, v in d.items()}

d = {'a': 1,
'b': 2,
'c': 3}
print(invert_dict(d))

# 12. Write a Python program to merge multiple dictionaries and sum the values of common keys.
print('Write a Python program to merge multiple dictionaries and sum the values of common keys.')
def merge_dicts(*dicts):
    result = {}
    for d in dicts:
        for k, v in d.items():
            if k in result:
                result[k] += v
            else:
                result[k] = v
    return result
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
print(merge_dicts(dict1,dict2))

# 13. Write a Python program to find the symmetric difference between two sets.
print('Write a Python program to find the symmetric difference between two sets.')
def symmetric_difference(set1, set2):
    return set1.symmetric_difference(set2)
set1 = {1,2,3,4}
set2 = {3,4,5,6}
print(symmetric_difference(set1, set2))

# 14. Write a Python function to find all subsets of a given set.
print('Write a Python function to find all subsets of a given set.')
def find_subsets(s):
    subsets = [[]]
    for elem in s:
        subsets += [subset + [elem] for subset in subsets]
        return subsets
s = {1,2,3}
print(find_subsets(s))
