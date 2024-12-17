def second_largest(arr):
    sorted_arr = sorted(arr)
    return sorted_arr[-2]


if __name__ == "__main__":
    arr = [10, 20, 4, 45, 99]
    print(f"Second largest element in the array {arr} is: {second_largest(arr)}")