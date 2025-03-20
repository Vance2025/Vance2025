



import re

a = 'PythocnPyhkt*&^hoKT123+Python'

def convert(value):
    matched = value.group()
    return '##' + matched + "&&"

b = re.sub('kt', convert, a, re.I)
print(b)

