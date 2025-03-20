



import re

a = 'PythocnPyhkt*&^hon12\n3+Python'

b = re.findall('KT*.{1}', a, re.IGNORECASE | re.S)
print(b)

