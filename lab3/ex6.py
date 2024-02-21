def find_common_elements(a, b):
    c=[]
    for elem in a:
        if elem in b:
            c.append(elem)
    return c