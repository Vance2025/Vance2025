WORDS = {'PAIR' : 4 , 'HAIR' : 4, 'CHAIR' : 5, 'GRAPHIC' : 7}

def main(): 
    print('Welcome to Spelling Bee!')
    print('Your leetrs are A I P C R H G')
    
    while len(WORDS) > 0:
        print(f'{len(WORDS)} words left!')
        guess = input('Guess a word: ')

        if guess == 'GRAPHIC':
            # clear()会清空字典中的key
            WORDS.clear()
            print('You\'ve won!')

        if guess in WORDS.keys():
            # pop()是字典的一个方法，可以返回字典中对应key的值，同时在下次查询字典时不再查询已匹配过的key。
            points = WORDS.pop(guess)               
            print(f'Good job! You scored {points} points!')

main()