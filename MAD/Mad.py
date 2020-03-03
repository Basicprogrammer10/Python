#Change the values in "num"
num = [63, 71, 65, 66, 87, 53]

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