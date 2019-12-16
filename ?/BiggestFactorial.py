
def factorial():
    b = c - 1
    c = c * b
def findfactorial():
    a = 1
    b = 1
    c = 0
    while True:
        a = a + 1
        print(a)
        c = a
        if b > 0:
            factorial()
findfactorial()
