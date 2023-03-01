
import sys
class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def is_empty(self):
        return self.items == []
    def peek(self):
        if not self.is_empty():
            return self.items[-1]

def tokenize(expr):
    for p in ['(',')','[',']','{','}']:
        expr = expr.replace(p, f' {p} ')
    return expr.split()
def is_balanced(expr):
    s = Stack()
    for token in tokenize(expr):
        if token in ['(', '[', '{']:
            s.push(token)
        elif token in [')', ']', '}']:
            if s.is_empty():
                return False
            p = s.pop()
            if p == '(' and token != ')':
                return False
            elif p == '[' and token != ']':
                return False
            elif p == '{' and token != '}':
                return False
    if not s.is_empty():
        return False
    return True

def evaluate_expression(stack):
    # Create an empty stack to hold operands
    operands = []
    # Create a dictionary to map operators to functions
    operators = {'+': lambda x, y: x + y,
                 '-': lambda x, y: x - y,
                 '*': lambda x, y: x * y,
                 '/': lambda x, y: x / y}
    # Loop through the stack
    for token in stack:
        if token == '(':
            # Do nothing, open parentheses are not operands or operators
            pass
        elif token == ')':
            # Pop the last two operands from the operand stack
            op2 = operands.pop()
            op1 = operands.pop()
            # Pop the next operator from the stack and apply it to the operands
            operator = operands.pop()
            result = operators[operator](op1, op2)
            # Push the result back onto the operand stack
            operands.append(result)
        elif token in operators:
            # Push the operator onto the operand stack
            operands.append(token)
        else:
            # Convert the operand from a string to a float and push it onto the operand stack
            operands.append(float(token))
    # The final result should be the only value left on the operand stack
    return operands[0]


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Input only 1 valid argument please.")
        sys.exit(1)
    
    expression = sys.argv[1]

    if (is_balanced(expression) == True):
        stack = Stack()  # create an instance of the Stack class
        for token in tokenize(expression):
            stack.push(token)  # push tokens into the stack
        # print(stack.items)  # print out the stack

        result = evaluate_expression(stack.items)
        print(result)
        
    else:
        print("Error, please input a valid argument.")