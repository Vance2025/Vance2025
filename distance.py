distance = {
    'Voyager 1' : 163,
    'Voyager 2' : 136,
    'Pioneer 10' : 80,
    'New Horizons' : 58,
    'Pioneer 11' : 44
}

def main():
    for name in distance.keys():
        print(f'The {name} is {convert(distance[name])} meters away from Earth.')


def convert(au):
    return au * 149597870700


main()
