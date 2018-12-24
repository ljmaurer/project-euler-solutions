def sumOfSquares(n):
    total = 0
    for i in range(n + 1):
        total += i * i
    return total
def squareOfSum(n):
    total = 0
    for i in range(n + 1):
        total += i
    total = total * total
    return total
answer = squareOfSum(100) - sumOfSquares(100)
print(answer)