import random

NUM_DIGITS = 3
MAX_GUESSES = 5

def main():
    print(
        f"""Bagles, a deductive logic game.

I am thinking of a {NUM_DIGITS}-digit number with no repeated digits.
Tr to guess what it is. Here are some clues

    When I say:   That means
    -----------------------------
    Pico          one digit is correct but in the wrong position
    Fermi         one digit is correct but in the right position
    Bagels        No digit is correct

For example, if the secret number was 248 and your guess was 843, the clues would be Fermi Pico.""")

    while True:
        secret_num =  get_secret_num()
        print('I have thought up a number')
        print(f'You have {MAX_GUESSES} guesses to get it.')

        num_guesses = 1
        while num_guesses <= MAX_GUESSES:
            guess = ''

            # keep guessing until they enter a valid guess
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print(f'Guess #{num_guesses}')
                guess = input('< ')
            
            clues = get_clues(guess, secret_num)
            print(clues)
            num_guesses += 1

            if guess == secret_num:
                break
            if num_guesses > MAX_GUESSES:
                print('You ran out of guesses')
                print(f'The answer was {secret_num}')
        
        # ask the player if they want to play again
        print('Do you want to play again? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break
    print('Thanks for playing!')


def get_secret_num():
    """Returns a string made up of NUM_DIGITS unique random digits"""
    numbers = list(range(0, 9))
    random.shuffle(numbers)

    # get the first `NUM_DIGITS` in the list for the secret number
    secret_num = ''
    for i in range(NUM_DIGITS):
        secret_num += str(numbers[i])
    return secret_num


def get_clues(guess, secret_num):
    """Returns a string with the pico, fermi, bagels clues for a guess and secret number pair."""
    if guess == secret_num:
        return 'You got it!'
    
    clues = []
    for idx, value in enumerate(guess):
        if value == secret_num[idx]:
            # a correct digit is in correct place
            clues.append('Fermi')
        elif value in secret_num:
            # a correct digit is in incorrect place
            clues.append('Pico')
    
    if len(clues) == 0:
        return 'Bagels' # there are no correct digits at all
    else:
        # sort the clues into alphabetical order so their original order doesn't give information away
        clues.sort() # nlogn
        return ' '.join(clues)


if __name__ == '__main__':
    main()