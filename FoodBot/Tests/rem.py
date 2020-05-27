def rem(words,stopwords):
    words2 = []
    nose = 0
    for word in list(words):  # iterating on a copy since removing will mess things up
        if word in stopwords:
            if nose == 0:
                words.remove(word)
                words2.append(word)
            else:
                pass
                #words.append(word)
            for word in list(words2):  # iterating on a copy since removing will mess things up
                if word in stopwords:
                    nose = 1
    return words;

a = ['1', '2', '1', '2', '3']
print(rem(a,'2'))