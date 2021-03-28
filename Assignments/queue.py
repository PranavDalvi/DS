def insert(q, max, rear, val):
    if rear >= max:
        print("Queue Full")
    else:
        q.append(val)
        rear += 1
        return rear

def delete(q, front, rear):
    if front == rear:
        print("Queue Empty")
    else:
        print(f"Popped element: {q[front]}")
        q.pop(front)
        front += 1
        return front

def display(q, front, rear):
    if front == rear:
        print("Queue Empty")
    else:
        print(f"Updated Queue: {q}")

# Driver Code

front = 0
rear = 0
max = 100

q = []
n = int(input("Enter number of elements: "))
for i in range(n):
    ele = int(input(f"Enter element no. {i}: "))
    q.append(ele)
    rear += 1

insert(q, max, rear, 100)
insert(q, max, rear, 1000)

display(q, front, rear)

delete(q, front, rear)

display(q, front, rear)

# Output
# Enter number of elements: 5
# Enter element no. 0: 1
# Enter element no. 1: 2
# Enter element no. 2: 3
# Enter element no. 3: 4
# Enter element no. 4: 5
# Updated Queue: [1, 2, 3, 4, 5, 100, 1000]
# Popped element: 1
# Updated Queue: [2, 3, 4, 5, 100, 1000]