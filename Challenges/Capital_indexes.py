#Solved!
def capital_indexes(string):
    capital = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    num = 0
    done = []
    for i in string:
        if any(i in s for s in capital):
            done.append(num)
        num = num + 1
    return done

print(capital_indexes("HeLlO"))