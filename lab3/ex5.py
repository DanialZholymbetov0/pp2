def is_prime(a):
    if a <= 1:
        return False
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            return False
    return True

def filter_prime(b):
    return [a for a in b if is_prime(a)]

b = list(map(int, input().split()))
primes = filter_prime(b)
print(primes)