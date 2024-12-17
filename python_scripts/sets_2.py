def findSubset(set1):
    subset = []
    for i in range(2**len(set1)):
        subset.append(tuple(set1[j] for j in range(len(set1)) if (i & (1 << j))))
    return subset

if __name__ == "__main__":
    set1 = [1, 2, 3]
    print(findSubset(set1))