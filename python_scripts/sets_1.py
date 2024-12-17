def symmetric_diff(set1, set2):
    set3 = set1^set2
    return set3

if __name__ == '__main__':
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}
    print(symmetric_diff(set1, set2))