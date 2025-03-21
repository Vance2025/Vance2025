# x = int(input('input the x: '))

# if x % 2 == 0:
#     print(f'{x} is even')
# else:
#     print(f'{x} is odd')



def main():
    x = int(input('input the x: '))
    if is_even(x):
        print(f'{x} is even')
    else:
        print(f'{x} is odd')

# def is_even(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False

# def is_even(n):
#     # return True if n % 2 == 0 else False

main()