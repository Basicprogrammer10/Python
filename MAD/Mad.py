#Change the values in "num"
num = [172, 122, 118, 188, 131, 197, 193, 157, 105, 155]

mean = 0
mad = []

for i in range(len(num)):
    mean = mean + num[i]
mean = mean / len(num)

for i in range(len(num)):
    mad.append(num[i] - mean)

for i in range(len(mad)):
    if mad[i] < 0:
        mad[i] = mad[i] * -1
mean = 0
for i in range(len(mad)):
    mean = mean + mad[i]
mean = mean / len(mad)
print(num)
print(mad)
print("----------")
print(mean)