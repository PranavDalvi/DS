def insertion_sort(a,n):
    for i in range(1,n):
        temp = a[i]
        j = i - 1
        while j >= 0 and a[j] > temp:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = temp

a = []
n = int(input("Enter number of elements: "))
for i in range(n):
    ele = int(input(f"Enter element no. {i}: "))
    a.append(ele)

insertion_sort(a,n)

print(f"Sorted output: {a}")

# Output
#Enter number of elements: 5
#Enter element no. 0: 12
#Enter element no. 1: 10
#Enter element no. 2: 11
#Enter element no. 3: 21
#Enter element no. 4: 05
#Sorted output: [5, 10, 11, 12, 21]