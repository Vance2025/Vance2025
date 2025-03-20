from enum import Enum

class VIP(Enum):
    YELLOW = 1
    YELLOW_ALT = 1
    BLACK = 3
    RED = 4

for s in VIP:
    print(s)

for s in VIP.__members__:
    print(s)