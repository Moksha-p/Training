def check_anagram(str1, str2):
    sorted_str1 = ''.join(sorted(str1))
    sorted_str2 = ''.join(sorted(str2))

    return sorted_str1 == sorted_str2
if __name__ == '__main__':
    s1 = 'silent'
    s2 = 'listen'
    print(f"'{s1}' and '{s2}' are anagrams: {check_anagram(s1, s2)}")
