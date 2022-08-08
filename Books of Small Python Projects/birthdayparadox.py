import datetime, random

def get_birthdays(number_of_birthdays):
    """Returns a list of number random date objects for birthdays"""
    birthdays = []

    for i in range(number_of_birthdays):
        # the year is unimportant for our simulation, as long as all
        # birthdays have the same year
        start_of_year = datetime.date(year=2024, month=1, day=1) # (2024, 1, 1)

        # get a random day into the year
        random_number_of_days = datetime.timedelta(random.randint(0, 364)) # day=randomNumber
        birthday = start_of_year + random_number_of_days # (2024, month, 1+randomNumber)
        birthdays.append(birthday)

    return birthdays


def get_match(birthdays):
    """Returns the date object of a birthday that occurs more than once in the birthdays list."""
    if len(birthdays) == len(set(birthdays)):
        # when all birthdays are unique
        return None
    
    # compare each birthday to every other birthday
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a + 1:]):
            if birthdayA == birthdayB:
                # return the matching birthday
                return birthdayA


# display the intro
print("""

The Birthday Paradox shows us that in a group of N people, the odds
that two of them have matching birthdays is surprisingly large.
This program does a Monte Carlo simulation (that is, repeated random
simulations) to explore this concept.

(It's not actually a paradox, it's just a surprising result.)
""")

# set up a tuple of month names in order
MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

while True:
    response = input('How many birthdays shall I generate? (max 100)> ')
    if response.isdecimal() and (0 < int(response) < 100):
        number_birthdays = int(response)
        break
print()

# generate and display birthdays
print(f'Here are {number_birthdays} birthdays: ')
birthdays = get_birthdays(number_birthdays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        # display a comma for each birthday after first birthday
        print(', ', end='')
    
    month_name = MONTHS[birthday.month - 1]
    date_text = f'{month_name} {birthday.day}'
    print(date_text, end='')
print()
# print()

# determine if there are 2 birthdays that match
match = get_match(birthdays)

# display the results
print('In this simulation, ', end='')

if match != None:
    month_name = MONTHS[match.month - 1]
    date_text = f'{month_name} {match.day}'
    print(f'Multiple people have a birthday on {date_text}')
else:
    print('There are no matching birthdays')
print()

# run through 100_000 simulations
print(f'Generating, {number_birthdays}, random birthdays 100_000 times...')
input('Press enter to begin...')

print("Let's run another 100_000 simulations")
sim_match = 0
sim_number = 100_000

for i in range(sim_number):
    if i % 10_000 == 0:
        print(f'{i} simulations run...')
    birthdays = get_birthdays(number_birthdays)
    if get_match(birthdays) != None:
        sim_match += 1
print('100,000 simulations run')

# display simulation results
probability = round(sim_match/sim_number * 100, 2)
print(f"""
Out of 100,000 simulations of {number_birthdays}, people, there was a
matching birthday in that group {sim_match} times.
This means that {number_birthdays} people have a {probability}% chance of having a matching birthday in their group.
""")
print("that's problably more than you think")

