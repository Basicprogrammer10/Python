from PIL import Image, ImageDraw, ImageFont
import re

text = 'This is a long string to test my program'

text = text + " "*25
textarray = []
formatted = []
hold = ''
num = 0

for i in text:
    textarray.append(i)

formatted = re.findall('.........................', text)

print(formatted)

out = Image.new("RGB", (822, 1122), (255, 255, 255))
fnt = ImageFont.truetype('C:\\Users\\turtl\\Mine-imator\\Data\\opensans.ttf', 75)
d = ImageDraw.Draw(out)

for i in formatted:
    print(i)
    d.multiline_text((0,num*75), str(i), font=fnt, fill=(0, 0, 0))
    num = num + 1

#out.save("test.png")
out.show()