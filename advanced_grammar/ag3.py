origin = 0

def distance(step):
    global origin
    new_distance = origin + step
    origin = new_distance
    return origin

print(distance(3))
print(distance(4))
print(distance(5))