def combination_and_sum(tup, target):
    result = []
    stack = [(0, [], target)]  
    tuple_data = sorted(tup)  
    
    while stack:
        index, path, remaining = stack.pop()
        
        if remaining == 0:
            result.append(tuple(path))  
            continue
        
        for i in range(index, len(tuple_data)):
            if i > index and tuple_data[i] == tuple_data[i - 1]:  
                continue
            if remaining - tuple_data[i] >= 0:
                stack.append((i + 1, path + [tuple_data[i]], remaining - tuple_data[i]))
    
    return result

if __name__ == "__main__":
    tup = (1, 2, 2, 3, 3, 4)
    target = 6
    print(combination_and_sum(tup, target))