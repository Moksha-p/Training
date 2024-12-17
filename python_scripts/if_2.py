import cmath  

def solve_quadratic(a, b, c):
    if a == 0:
        return "Not a quadratic equation"  
    
    discriminant = b**2 - 4*a*c
    
    if discriminant > 0:
        root1 = (-b + discriminant**0.5) / (2 * a)
        root2 = (-b - discriminant**0.5) / (2 * a)
        return f"Real roots: {root1}, {root2}"
    elif discriminant == 0:
        root = -b / (2 * a)
        return f"Equal roots: {root}"
    else:
        root1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
        root2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
        return f"Complex roots: {root1}, {root2}"
    
if __name__ == "__main__":
    a = 1; b  = -3; c = 2
    print(solve_quadratic(a, b, c))    