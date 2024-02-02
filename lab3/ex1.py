def calculate_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:     
        return n * calculate_factorial(n - 1)
a=int(input())
result = calculate_factorial(a)
print(result)
