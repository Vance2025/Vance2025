import re

a = 'ASD289764644654ABGC'


b = re.match('\d', a)
print(b)

c = re.search('\d', a)
print(c.group())

