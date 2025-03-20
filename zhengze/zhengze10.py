import re

s = 'Life is short, I use Python, I love Python'
m = re.search('Life(.*)Python(.*)Python', s)

print(m.groups())
