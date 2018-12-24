import math
def sumOfDigits(n):
    result = 0
    while n >= 1:
        result += n % 10
        n = math.floor(n / 10)
    return result
print(sumOfDigits(math.floor(math.pow(2, 1000))))