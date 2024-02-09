def calculate_running_average(a):
    b=[a[0]]
    for i in range (1, len(a)):
        b.append((b[i-1]*i + a[i])/(i + 1))
    return b