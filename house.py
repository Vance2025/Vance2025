name = input('Enter your name: ')

# if name == 'Alice':
#     print('Hello, Alice!')
# elif name == 'Bob':
#     print('Hello, Bob!')
# else: 
#     print('Hello, stranger!')



match name:
    case 'Alice':
        print('Hello, Alice!')
    case 'Bob':
        print('Hello, Bob!')
    case _:
        print('Who?')
