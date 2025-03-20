

import re

a = 'python|c++|java|c#|javascript'

b = re.findall('php', a)
if len(b) > 0:
    print('字符串中包含python')
else:
    print('字符串中无此字符串')
