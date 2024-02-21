def abc(n):
    for i in reversed(range(int(n))):
        yield i
n=input()
generator=abc(n)
for i in generator:
    print((i))        