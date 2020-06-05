#Solved
def mid(string):
    mid = len(string)%2
    array = []
    for i in string:
        array.append(i)
    if mid == 0:
        return 
    else:
        middle = (len(array) - 1)/2
        return array[int(middle)]


print(mid("abcde"))

