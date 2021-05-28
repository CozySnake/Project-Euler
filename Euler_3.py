# Don't try to run it, It takes time to find a solution!

total = 0
for num in range(3, int(600851475143/2+0.5), 2):
    for n in range(3, num, 2):
        if num == n:
            continue
        if num%n==0:
            break
    else:
        if 600851475143%num==0:
            total = num
            print(total)
print(total, "last result")