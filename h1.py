name = input('Pease enter your name: ')

name = name.strip()
name = name.title()

first, last = name.split(' ')

print(f'Hello, {last}')
print(f'Hello, {first}')
print(f'Hello, {name}')
