def divisors(n):
    result = list()
    for i in range(1, n):
        if n % i == 0:
            result.append(i)
    return result

def sumDivs(n):
    result = 0
    divN = divisors(n)
    for i in range(len(divN)):
        result += divN[i]
    return result

def amicable(a, b):
    if sumDivs(a) == b and sumDivs(b) == a:
        return True
    return False

for i in range(1, 10000):
    for j in range(1, i):
        if amicable(i, j):
            print(i)
            print(j)