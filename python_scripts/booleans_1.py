def evaluate(expr):
    sum = 0
    for e in expr:
        if eval(e):
            sum += 1
    return sum

if __name__ == '__main__':
    expr = ["True", "False", "True", "True", "False"]
    print(evaluate(expr))