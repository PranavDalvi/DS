
def push(i,size):
    stk.append(i)
    size = size + 1

def pop(size):
    if stk == []:
        return 0
    else:
        size -= 1
        return stk.pop()

def seek(size):
    if stk == []:
        return False
    else:
        return stk[size]

def evaluate(expr):
    for i in expr:
        if i in "0123456789":
            push(i, size)
        else:
            a1 = pop(size)
            a2 = pop(size)
            result = calculation(a2, a1, i)
            push(result, size)
    return pop(size)

def calculation(a2, a1, i):
    if i == "*":
        return int(a2) * int(a1)
    elif i == "/":
        return int(a2) / int(a1)
    elif i == "+":
        return int(a2) + int(a1)
    elif i == "-":
        return int(a2) - int(a1)

stk=[]
size = -1
expr = input("Enter the postfix expression: ")

value = evaluate(expr)

print(f"The result of postfix expression for {expr} is {value}")

# Output
# Enter the postfix expression: 23+5*
# The result of postfix expression for 23+5* is 25