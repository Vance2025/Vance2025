emoji = '*^_^*'

def main():
    global emoji
    say('Anyone?')
    emoji = '^;^'
    say('I\'m here!')

def say(message):
    print(message, emoji)

say('Anyone?')
main()
