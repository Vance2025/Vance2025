def traveller():
    x = 0
    def travel(step):
        nonlocal x
        x += step
        return x
    return travel

distance_traveller1 = traveller()
distance_traveller2 = traveller()

print('The distance of Traveller 1 is: ' + str(distance_traveller1(3)))
print('The distance that traveller 2 spaned is: ' + str(distance_traveller2(5)))



