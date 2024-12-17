def invert_dict(dict):
    inverted_dict = {}
    for key, val in dict.items():
        inverted_dict[val] = key
    
    return inverted_dict

if __name__ == "__main__":
    original_dict = {'a': 1, 'b': 2, 'c': 3}
    inverted_dict = invert_dict(original_dict)
    print(f"Original Dictionary: {original_dict}")
    print(f"Inverted Dictionary: {inverted_dict}")