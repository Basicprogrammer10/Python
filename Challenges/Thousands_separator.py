def format_number(number):
    array = []
    for i in str(number):
        array.append(str(i))
    rev = reversed(array)
    if len(array) <= 4:
        num = 1
        for c in reversed(array):
            if num == 3:
                print(num)
                array.insert(num, ',')
            num = num + 1
    print("".join(array))

format_number(1000)

a = [1, 2, 4]
a.insert(2, ",")