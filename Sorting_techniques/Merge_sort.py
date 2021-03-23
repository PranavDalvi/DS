def merge(a, low, mid, high):
    n1 = mid - low + 1
    n2 = high - mid
    
    # create temp arrays
    L = [0] * (n1)
    H = [0] * (n2)

    # Copy data to temp arrays
    for i in range(0, n1):
        L[i] = a[low + i]
    for j in range(0, n2):
        H[j] = a[mid + 1 + j]
    
    i = 0 # initial index of first subarray
    j = 0 # initial index of second subarray
    k = low # initial index of merged subarray

    while i < n1 and j < n2:
        if L[i] <= H[j]:
            a[k] = L[i]
            i += 1
        else:
            a[k] = H[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[] if any
    while i < n1:
        a[k] = L[i]
        i += 1
        k += 1
    
    # Copy the remaining elements of H[] if any
    while j < n2:
        a[k] = H[j]
        j += 1
        k += 1

def merge_sort(a, low, high):
    if (low < high):
        mid = (low + (high - 1)) //2
        merge_sort(a, low, mid)
        merge_sort(a, mid + 1, high )
        merge(a, low, mid, high)

a = []
n = int(input("Enter number of elements: "))
for i in range(n):
    ele = int(input(f"Enter element no. {i}: "))
    a.append(ele)

merge_sort(a, 0, n-1)

print(f"Sorted output: {a}")

#Output
#Enter number of elements: 5
#Enter element no. 0: 1
#Enter element no. 1: 56
#Enter element no. 2: 2
#Enter element no. 3: 89
#Enter element no. 4: 34
#Sorted output: [1, 2, 34, 56, 89]
