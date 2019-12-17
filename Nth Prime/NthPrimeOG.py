num = 1
p = []
f = int(input("Prime Number: "))
while f != len(p):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            p.append(num)
    num = num + 1
print(p[f-1])