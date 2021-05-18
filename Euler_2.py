a = 0
b = 1
total = 0

while b < 4000000:
    c = b
    b = b + a
    a = c
    #print(a, end=" ")
    if a % 2 == 0:
        total += a
        print(a, "-", total, end=" / ")

print("\n", total)
#c=1, a=1, b=1  ////  c=1, b=2, a=1   ////   c=2, b=3, a=2