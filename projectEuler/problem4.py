import math
def digits(n):
    result = list()
    while n >= 1:
        result.append(n % 10)
        n = math.trunc(n / 10)
    return result
def palindrome(n):
    check = digits(n)
    while len(check) >= 1:
        if check[0] != check[len(check) - 1]:
            return False
        check.pop(0)
        if len(check) > 0:
            check.pop()
    return True
answer = 0
for i in range(100, 999):
    for j in range(100, 999):
        if i * j > answer and palindrome(i * j):
            answer = i * j
print(answer)

      
    

        