def abc(n):
    for i in range(int(n)):
        yield i**2
n=input()
Generator=abc(n)
for i in Generator:
    print(i)