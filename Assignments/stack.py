
def push(stk, max, top, val):
    if top >= max:
        print("Stack Overflow")
    else:
        stk.append(val)
        top += 1
        return top

def pop(stk, top):
    if top <= 0:
        print("Stack Underflow")
    else:
        x = stk.pop()
        top -= 1
        print(f"Popped element: {x}")
        return top 

def peek(stk, top):
    if top == 0:
        print("Empty Stack")
    else:
        print(f"top = {stk[top]}")

        print(f"Updated stack = {stk}")

# Driver code
top = 0
max = 100

stk = []
n = int(input("Enter number of elements: "))
for i in range(n):
    ele = int(input(f"Enter element no. {i}: "))
    stk.append(ele)
    top += 1

push(stk, max, top, 100)
push(stk, max, top, 1000)

peek(stk, top)

pop(stk, top)

peek(stk, top)

# Output
# Enter number of elements: 5
# Enter element no. 0: 1
# Enter element no. 1: 2
# Enter element no. 2: 3
# Enter element no. 3: 4
# Enter element no. 4: 5
# top = 100
# Updated stack = [1, 2, 3, 4, 5, 100, 1000]
# Popped element: 1000
# top = 100
# Updated stack = [1, 2, 3, 4, 5, 100]