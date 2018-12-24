def isPythag(a, b, c):
    if a * a + b * b == c * c:
        return True
    return False
def sumToThousand(a, b, c):
    if a + b + c == 1000:
        return True
    return False
for c in range(1, 1000):
    for b in range(1, c):
        for a in range(1, b):
            if isPythag(a, b, c) and sumToThousand(a, b, c):
                print(a * b * c)