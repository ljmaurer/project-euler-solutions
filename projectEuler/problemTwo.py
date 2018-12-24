i = 2
fibs = [1, 2]
curr = 2
while curr < 4000000:
    curr = fibs[i - 1] + fibs[i - 2]
    i += 1
    fibs.append(curr)
total = 0
for j in range(len(fibs)):
    if fibs[j] % 2 == 0:
        total += fibs[j]
print(total)