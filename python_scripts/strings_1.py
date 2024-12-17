def find_longest_word(s):
    words = s.split()
    longest_word = ""
    max_len = 0

    for word in words:
        if len(word) > max_len:
            longest_word = word
            max_len = len(word)

    return longest_word

if __name__ == "__main__":
    s = "The quick brown fox jumped over the lazy dog"
    print(f"The longest word in the sentence '{s}' is: {find_longest_word(s)}")