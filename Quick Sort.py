def partition(a,l,u): # a = Array, l = Lower bound, u = upper bound 
    p = a[l]
    i = l
    j = u
    while i < j:
        while a[i] <= p and i <= u:
            i += 1
        while a[j] > p and j >= l:
            j -= 1
        if i < j:
            a[i], a[j] = a[j], a[i]
        a[j], a[l] = a[l], a[j]
        return j

def quick_sort(a,l,u):
    if (1 < u):
        j = partition(a,l,u)
        quick_sort(a,l,j - 1) # left half of pivot
        quick_sort(a,l,j + 1) # right half of pivot

a = []
n = int(input("Enter number of elements: "))
for i in range(n):
    ele = int(input(f"Enter element no. {i}: "))
    a.append(ele)

quick_sort(a, 0, n-1)
print(f"Sorted output: {a}")

# Output
# Enter number of elements: 5
# Enter element no. 0: 10
# Enter element no. 1: 4  
# Enter element no. 2: 2
# Enter element no. 3: 11
# Enter element no. 4: 23
# Sorted output: [2, 4, 10, 11, 23]
