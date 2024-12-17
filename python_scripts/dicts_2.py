def add_dicts(dict1, dict2):
    for k, v in dict2.items():
        if k in dict1:
            dict1[k] += v
        else:
            dict1[k] = v

    return dict1

if __name__ == '__main__':
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'b': 3, 'c': 4, 'd': 6}
    print(add_dicts(dict1, dict2))