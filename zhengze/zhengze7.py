import re

a = '13289764644654ABGC'

def convert(value):
    matched = value.group()
    if int(matched) >= 6:
        matched = 9
    else:
        matched = 0
    return str(matched)

b = re.sub('\d', convert, a)
print(b)

