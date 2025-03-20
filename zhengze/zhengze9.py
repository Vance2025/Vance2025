import re

s = 'Life is short, I use Python, I love Python'
m = re.findall('Life(.*)Python', s)
# print(m.group())
print(m)
