# while True:
#     n = int(input('How many times do you want the cat to Meow to you?  '))
#     if n > 0:
#         break

# for _ in range(n):
#     print('Meow!')


def main():
    number = get_number()
    meow(number)


def get_number():
    while True:
        n = int(input('How many times do you want the cat to Meow to you?  '))
        if n > 0:
            return n

def meow(n):
    for _ in range(n):
        print('Meow!')

main()


