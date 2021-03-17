def bubble_sort(a,n):
    swapped = 0
    i = 0
    while i < n - 1 and swapped == 0:
        swapped = 1
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1],a[j]# Exchange the adjacent values
                swapped = 0
        i = i + 1


a = []
n = int(input("Enter number of elements: "))
for i in range(n):
    ele = int(input(f"Enter element no. {i}: "))
    a.append(ele)

bubble_sort(a,n)

print(f"Sorted output: {a}")

#Output
#Enter number of elements: 5
#Enter element no. 0: 50
#Enter element no. 1: 12
#Enter element no. 2: 18
#Enter element no. 3: 45
#Enter element no. 4: 89
#Sorted output: [12, 18, 45, 50, 89]