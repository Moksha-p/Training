import itertools

def gen_permutations(arr):
    return list(itertools.permutations(arr))

if __name__ == "__main__":
    arr = [1, 2, 3]
    print(gen_permutations(arr))