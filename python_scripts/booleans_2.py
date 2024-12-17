def eval_boolean(expr):
    return eval(expr)

if __name__ == '__main__':
    expr = 'True and False or True'
    print(eval_boolean(expr))