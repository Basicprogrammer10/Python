from random import randint
class text:
    low = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z', ' ']
    hi  = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z', ' ']
    def MakeBig(lower, low=low,hi=hi):
        done = []
        final = ''
        for i in lower:
            done.append(hi[low.index(i)])
        for i in done:
            final = final + i
        return final
    def MakeNotBig(lower,low=low,hi=hi):
        done = []
        final = ''
        for i in lower:
            done.append(low[hi.index(i)])
        for i in done:
            final = final + i
        return final
    def Random(lower,low=low,hi=hi):
        done = []
        final = ''
        for i in lower:
            x = randint(0,1)
            if x == 1:
                done.append(low[low.index(i)])
            else:
                done.append(hi[low.index(i)])
        for i in done:
            final = final + i
        return final

print(text.Random("its not a problem anymore"))