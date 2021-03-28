def fact(n):
    if n == 0:
        return 1
    else:
        return(n * fact(n-1))

n = int(input("Enter any number: "))
print(fact(n))

# output
# Enter any number: 5
# 120
#
# Enter any number: 2
# 2
# 
# Enter any number: 10
# 3628800