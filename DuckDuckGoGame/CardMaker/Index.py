from PIL import Image, ImageDraw, ImageFont

text = 'Hello World! This is a test so yeah...'

textarray = []
formatted = []
hold = ''
num = 23

for i in text:
    textarray.append(i)


def formater(num,hold,text,formatted):
    #print("Text: " + str(text))
    for i in text:
        if num > 24:
            #print(str(text[num:]))
            end = ''
            for i in str(text[num:]):
                end = end + i
            #hold = text[num:]
            #formatted.append(formater(0,'',str(text[num:]),[]))
            hold = formater(0,'',end,[])
            break
        else:
            hold = hold + i
        num = num + 1
    formatted.append(hold)
    num = 0
    return formatted

#formatted = formater(num,hold,textarray,formatted)
print(formater(num,hold,textarray,formatted))

def Image(num,formatted):
    out = Image.new("RGB", (822, 1122), (255, 255, 255))
    fnt = ImageFont.truetype('C:\\Users\\turtl\\Mine-imator\\Data\\opensans.ttf', 75)
    d = ImageDraw.Draw(out)

    for i in formatted:
        d.multiline_text((0,num*75), i, font=fnt, fill=(0, 0, 0))
        num = num + 1

    #out.save("test.png")
    out.show()