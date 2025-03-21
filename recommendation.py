# def main():
#     dificulty = input('Hard or Easy? ')
#     players = input('How many players? ')

#     if dificulty == 'Hard':
#         if players == '1':
#             recommed('Poker')
#         else:
#             recommed('Chess')
#     elif dificulty == 'Easy':
#         if players != '1':
#             recommed('Solitaire')
#         else:
#             recommed('Go Fish')
 
#     else:
#         print('Maybe you should try other difficulty or number of players.')



def main():
    dificulty = input('Hard or Easy? ')
    if not (dificulty == 'Hard' or dificulty == 'Easy'):
        print('Invalid input')
        return
    elif dificulty == 'Hard':
        players = int(input('How many players? '))
        if 1 <= players <= 4:
            recommed('Poker')
        else:
            recommed('Chess')
    else:
        players = int(input('How many players? '))
        if 1 <= players <= 4:
            recommed('Solitaire')
        else:
            recommed('Go Fish')




def recommed(game):
    print(f'I\'d recommend you to play {game}')

main()
