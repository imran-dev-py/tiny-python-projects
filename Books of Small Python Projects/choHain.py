import random, sys

JAPANESE_NUMBERS = {
    1: 'ICHI',
    2: 'NI',
    3: 'SAN',
    4: 'SHI',
    5: 'GO',
    6: 'ROKU',
}

print(
    """In this traditional Japanese dice game, two dice are rolled in a bamboo
cup by the dealer sitting on the floor. The player must guess if the
dice total to an even (cho) or odd (han) number."""
)
print()

purse = 5000

while True:
    # place your bet
    print(f'You have {purse} mon. How much do you bet? (or QUIT)')

    # checking for valid bet
    while True:
        bet_mon = input('> ')
        if bet_mon.upper() == 'QUIT':
            print('Thanks for playing')
            sys.exit()
        elif not bet_mon.isdecimal():
            print('Please enter a number')
        elif int(bet_mon) > purse:
            print('You do not have enough to make that bet')
        else:
            # this is valid bet
            bet_mon = int(bet_mon)
            break
    
    # roll the dice
    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)

    print(f'The dealer swirls the cup and you hear the rattle of dice.\n'
    f'The dealer slams the cup on the floor, still covering the\n'
    f'dice and asks for your bet.')
    print()
    print(f"{(' ' * 7)}CHO (even) or HAN (odd)?")

    # let the player bet on cho or han
    while True:
        on_bet = input('> ').upper()
        if on_bet != 'CHO' and on_bet != 'HAN':
            print('Please enter either "CHO" or "HAN"')
            continue
        else:
            break
    
    # Reveal the dice results
    print('The dealer lifts the cup to reveal.')
    print(f"{(' ' * 2)}{JAPANESE_NUMBERS[dice_1]} - {JAPANESE_NUMBERS[dice_2]}")
    print(f"{(' ' * 4)}{dice_1} - {dice_2}")

    # determine if the player won
    roll_is_even = (dice_1 + dice_2) % 2 == 0
    if roll_is_even:
        correct_bet = 'CHO'
    else:
        correct_bet = 'HAN'
        
    player_won = on_bet == correct_bet

    # display the bet results
    if player_won:
        print(f'You Won! You take {bet_mon} mon.')
        # add bet_money from player's purse
        purse += bet_mon
        house_own = bet_mon // 10
        print(f"The house collects {house_own} mon fee.")
        # house fee 10%
        purse -= house_own
    else:
        purse -= bet_mon
        print('You lost!')
    
    # check if the player is run out of money
    if purse == 0:
        print('You have run out of monney!')
        print('Thanks for playing!')
        sys.exit()





