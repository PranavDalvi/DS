# Linear search code part 1
def linearSearch(a,x):
    for i in range(len(a)):
        if a[i] == x:
            
            return i

    return -1

# Common driver code
a = []
x = int(input("Enter the element you want to search: "))
n = int(input("Enter number of elements: "))
for i in range(n):
    ele = int(input(f"Enter element no. {i}: "))
    a.append(ele)

# Linear search code part 2
res = linearSearch(a,x)

if res == -1:
    print("Element Not Found")
else:
    print("Element Found")

# Output 1
# Enter the element you want to search: 20
# Enter number of elements: 5
# Enter element no. 0: 10
# Enter element no. 1: 20
# Enter element no. 2: 30
# Enter element no. 3: 40
# Enter element no. 4: 50
# Element Found

# Output 2
# Enter the element you want to search: 60
# Enter number of elements: 5
# Enter element no. 0: 10
# Enter element no. 1: 20
# Enter element no. 2: 30
# Enter element no. 3: 40
# Enter element no. 4: 50
# Element Not Found