def collatz_sequence(number):
    if number <= 0:
        return "Input must be a positive integer."
    
    sequence = [number]  
    while number != 1:
        if number % 2 == 0:  
            number = number // 2
        else:  
            number = 3 * number + 1
        sequence.append(number)  
    return sequence

if __name__ == "__main__":
    num = 13
    print(f"Collatz sequence for {num}: {collatz_sequence(num)}")
