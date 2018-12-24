def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
print(isPrime(5))
print(isPrime(17))
print(isPrime(20))
print(isPrime(2))

curr = 0 
for j in range(3, 600851475143):
    if j > curr and isPrime(j) and 600851475143 % j == 0:
        curr = j
print(curr)

"""
lmaurer
logan2code
"""
