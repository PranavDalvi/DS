def bubble_sort(a,n):
    for i in range(n-1):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j] # Exchange the adjacent values


a = []
n = int(input("Enter number of elements: "))
for i in range(n):
    ele = int(input(f"Enter element no. {i}: "))
    a.append(ele)

bubble_sort(a,n)

print(f"Sorted output: {a}")

#output
#Enter number of elements: 5
#Enter element no. 0: 10
#Enter element no. 1: 20
#Enter element no. 2: 1
#Enter element no. 3: 4
#Enter element no. 4: 6
#Sorted output: [1, 4, 6, 10, 20]