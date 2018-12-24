import math
factorials = [1]
def factorial(n):
    for i in range(1, n + 1):
        factorials.append(i * factorials[i - 1])
    return factorials[n]
def sumOfDigits(n):
    total = 0
    while n >= 1:
        total += n % 10
        n = math.floor(n / 10)
    return total
print(sumOfDigits(factorial(100)))