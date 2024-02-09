def find_common_elements(a, b):
    c = []
    for elem in a:
        if elem in b:
            c.append(elem)
    return c

a = list(map(int, input("Enter elements of list 'a' separated by space: ").split()))
b = list(map(int, input("Enter elements of list 'b' separated by space: ").split()))

result = find_common_elements(a, b)
print("Common elements:", result)
