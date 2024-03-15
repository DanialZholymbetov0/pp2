def multiply(n):
    res = 1
    for i in n:
        res *= i
    return res
n = list(map(int, input().split()))
abc = multiply(n)
print(abc)