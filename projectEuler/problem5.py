def isMult(n):
    for i in range(1, 20):
        if n % i != 0:
            return False
    return True
found = False
answer = 20
while not found:
    if not isMult(answer):
        answer = answer + 20
    else:
        found = True
print(answer)
    