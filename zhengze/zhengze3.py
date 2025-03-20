

# import re

# # container = 'abc, acc, afc, aec, adc, a9c'
# container = 'python 3216546java%$php'

# r = re.findall('[a-z]{3,5}?', container)
# print(r)


import re
container = 'pytho0python#pythonn%'
r = re.findall('python?', container)
print(r)