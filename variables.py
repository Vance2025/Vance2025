def get_guess():
    guess = input("Enter the number: ")
    return guess

def main():
    guess = int(get_guess())
    if guess >= 50:
        print("You win!")
    else:
        print("You lose!")

main()
