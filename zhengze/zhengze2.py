

import re

container = 'pytho4545454n|c++|jav^*&(a|c#|java435script'

digits = re.findall('\d', container)

non_digits = re.findall('\D', container)

print(digits)  

print(non_digits)  

