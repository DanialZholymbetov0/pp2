def abc(n):
    for i in range(int(n)):
        if (i%2==0):
            yield i
n=input()
generator=abc(n)
for i in generator:
    print(i, end=",")       