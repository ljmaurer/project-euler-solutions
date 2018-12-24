import math
def noDigits(n):
    return math.floor(math.log(n, 10)) + 1
fibs = [1, 1]
currIndex = 2
while noDigits(fibs[currIndex - 1]) < 1000:
    fibs.append(fibs[currIndex - 1] + fibs[currIndex - 2])
    currIndex += 1
print(currIndex)