# Binary search code part 1
def binarySearch(a,x):
    l = 0
    h = len(a) - l
    while(1 <= h):
        mid = (l + h) // 2
        if a[mid] == x:
            return mid      # Element x found at position mid
        elif a[mid] > x:
            h = mid - l     # Search in left half
        else:
            l = mid + l     # Search in right half
    return -1               # Element x not found

# Common driver code
a = []
x = int(input("Enter the element you want to search: "))
n = int(input("Enter number of elements: "))
for i in range(n):
    ele = int(input(f"Enter element no. {i}: "))
    a.append(ele)

# Binary search code part 2
res = binarySearch(a,x)

if res == -1:
    print("Not Found!")
else:
    print("Found!")


# Output 1
# Enter the element you want to search: 50
# Enter number of elements: 5
# Enter element no. 0: 10
# Enter element no. 1: 20
# Enter element no. 2: 40
# Enter element no. 3: 50
# Enter element no. 4: 60
# Found!

# Output 2
# Enter the element you want to search: 30
# Enter number of elements: 5
# Enter element no. 0: 10
# Enter element no. 1: 20
# Enter element no. 2: 40
# Enter element no. 3: 50
# Enter element no. 4: 60
# Not Found!