import math
def digitsBaseN(digitsOf, n):
    result = list()
    while digitsOf >= 1:
        result.append(digitsOf % n)
        digitsOf = math.floor(digitsOf / n)
    return result
def palindrome(digitsOf, baseIn):
    check = digitsBaseN(digitsOf, baseIn)
    while len(check) >= 1:
        if check[0] != check[len(check) - 1]:
            return False
        check.pop(0)
        if len(check) > 0:
            check.pop()
    return True
def doubleBasePalindrome(n):
    if palindrome(n, 2) and palindrome(n , 10):
        return True
    return False
answer = 0
for i in range(1000000):
    if doubleBasePalindrome(i):
        answer += i
print(answer)
    