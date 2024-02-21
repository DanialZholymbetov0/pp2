def abc(n,m):
    for i in range(int(n), int(m)):
        yield i**2
n=input()
m=input()
generator=abc(n,m)
for i in generator:
    print(i)        