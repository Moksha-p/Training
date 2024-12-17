def longest_increasing_subsequence(nums):
    n = len(nums)
    if n == 0:
        return []

    seq = [1] * n 
    parent = [-1] * n 

    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j] and seq[i] < seq[j] + 1:
                seq[i] = seq[j] + 1
                parent[i] = j

    max_length_index = max(range(n), key=lambda x: seq[x])

    result = []
    while max_length_index != -1:
        result.append(nums[max_length_index])
        max_length_index = parent[max_length_index]

    return result[::-1]

if __name__ == '__main__':
    nums = [10, 22, 9, 33, 21, 50, 41, 60, 80]
    print("Longes increasing sequence is", longest_increasing_subsequence(nums))