#match-case for each operation
# def match_op(item, operand1, operand2):
#     match item:
#         case '+':
#             results = operand1 + operand2
#             return results
#         case '-':
#             results = operand1 - operand2
#             return results
#         case '/':
#             results = operand1 / operand2
#             return results
#         case '*':
#             results = operand1 * operand2
#             return results
#         case '^':
#             results = operand1 ** operand2
#             return results
def add(operand1, operand2):
    int1 = int(operand1)
    int2 = int(operand2)
    results = int1 + int2
    return results

def subtract(operand1, operand2):
    int1 = int(operand1)
    int2 = int(operand2)
    results = int1 - int2
    return results

def divide(operand1, operand2):
    int1 = int(operand1)
    int2 = int(operand2)
    if int2 == 0:
        return "Error, cannot be divide by zero"
    else:
        results = int1 / int2
        return results

def multiply(operand1, operand2):
    int1 = int(operand1)
    int2 = int(operand2)
    results = int1 * int2
    return results
    
def power(operand1, operand2):
    int1 = int(operand1)
    int2 = int(operand2)
    results = int1 ** int2
    return results
