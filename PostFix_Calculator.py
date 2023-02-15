from StackedLinkedList import Stack
import ops

def postfix(postfixList):
    #create stack and a list of operations
    postfixStack = Stack()
    operator = ['+', '-', '*', '/', '^']
    
    #iterates each item in the postfixList
    for item in postfixList:
        #if the item in the list is not an operator, push it into the stack
        if item not in operator:
            postfixStack.push(item)
            postfixStack.peek() #peek to see if it's done correctly

        #if item is not an operator, then pop() item and assign it to operand based on when its popped()
        else:
            operand1 = int(postfixStack.pop())
            operand2 = int(postfixStack.pop())
            #calls match_op method to commit the operation
            if item == '+':
                results = (ops.add(operand1, operand2))
                #push the result of the operation into the stack
                postfixStack.push(results)              
            elif item == '-':
                results = ops.subtract(operand1, operand2) 
                postfixStack.push(results) 
            elif item == '*':
                results = ops.multiply(operand1, operand2) 
                postfixStack.push(results) 
            elif item == '/':
                results = ops.divide(operand1, operand2) 
                postfixStack.push(results) 
            elif item == '^':
                results = ops.power(operand1, operand2) 
                postfixStack.push(results) 
            else:
                print("Invalid operator")
    #returns final result
    return postfixStack.pop()

user = input("Enter a postfix expression with white spaces(ex. 3 6 +): ").replace(" ", "")
print(postfix(list(user)))
