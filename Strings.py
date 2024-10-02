
# Write a Python function to find the longest word in a given sentence.
def find_longest_word(sentence):
    words = sentence.split()  
    longest_word = max(words, key=len)  
    return longest_word

sentence = input("Enter a sentence: ")

longest = find_longest_word(sentence)
print(f"The longest word is: {longest}")



# Write a Python function to check if two given strings are anagrams of each other.
def are_anagrams(str1, str2):
   
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    return sorted(str1) == sorted(str2)


str1 = input("Enter the first string: ")
strEx = input("XYZ")
str2 = input("Enter the second string: ")


if are_anagrams(str1, str2):
    print(f'"{str1}" and "{str2}" are anagrams.')
else:
    print(f'"{str1}" and "{str2}" are not anagrams.')
