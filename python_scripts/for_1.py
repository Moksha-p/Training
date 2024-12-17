def generate_fibonacci(n):
    if n <= 0:
        return "Number of terms must be a positive integer."
    elif n == 1:
        return [0] 
    elif n == 2:
        return [0, 1] 
    
    fibonacci_series = [0, 1]  
    for _ in range(2, n):  
        next_term = fibonacci_series[-1] + fibonacci_series[-2]
        fibonacci_series.append(next_term)
    return fibonacci_series

if __name__ == "__main__":
    n = 5
    print(f"First {n} terms of Fibonacci sequence:")
    print(generate_fibonacci(n))
