# Program to count True values in a list of Boolean expressions:

def count_true_values(boolean_list):
    return boolean_list.count(True)

boolean_list = [True, False, True, True, False]
result = count_true_values(boolean_list)

print(f"Count of True values: {result}")


#2.Function to evaluate a complex Boolean expression represented as a string:

def evaluate_boolean_expression(expression):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        return f"Error in evaluating expression: {e}"

expression = "True and False or True"
result = evaluate_boolean_expression(expression)

print(f"Result of the expression '{expression}': {result}")
