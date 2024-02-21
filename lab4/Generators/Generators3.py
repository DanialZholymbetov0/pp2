def abc(n):
    for i in range(int (n)):
        if((i%3)==0)or((i%4)==0):
            yield i
n=input()
generator=abc(n)
for i in generator:
    print(i)            