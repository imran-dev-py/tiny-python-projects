from ctypes import resize
import random

# set up the constants
OBJECTIVE_PRONOUNS = ['Her', 'Him', 'Them']
POSSESSIVE_PRONOUNS = ['Her', 'His', 'Their']
PERSONAL_PRONOUNS = ['She', 'He', 'They']
STATES = ['California', 'Texas', 'Florida', 'New York', 'Pennsylvania', 'Illinois', 'Ohio', 'Georgia', 'North Carolina', 'Michigan']
NOUNS = ['Athlete', 'Clown', 'Shovel', 'Paleo Diet', 'Doctor', 'Parent', 'Cat', 'Dog', 'Chicken', 'Robot', 'Video Game', 'Avocado', 'Plastic Straw', 'Serial Killer', 'Telephone Psychic']
PLACES = ['House', 'Attic', 'Bank Deposit Box', 'School', 'Basement', 'Workplace', 'Donut Shop', 'Apocalypse Bunker']
WHEN = ['Soon', 'This Year', 'Later Today', 'RIGHT NOW', 'Next Week']
WHEN = []


def main():
    print('Clickbait Headline Generator')
    print()

    print('Our website needs to trick people into looking at ads!')

    while True:
        print('Enter the number of clickbait headlines generate')
        response = input('< ')

        if not response.isdecimal():
            print('Please enter a number')
        else:
            number_of_headlines = int(response)
            break

    print()
    for i in range(number_of_headlines):
        clickbait_type = random.randint(1, 8)

        clickbait_lines = {
            1: generateAreMillennialsKillingHeadline(),
            2: generateWhatYouDontKnowHeadline(),
            3: generateBigCompaniesHateHerHeadline(),
            4: generateYouWontBelieveHeadline(),
            5: generateDontWantYouToKnowHeadline(),
            6: generateGiftIdeaHeadline(),
            7: generateReasonsWhyHeadline(),
            8: generateJobAutomatedHeadline(),
        }

        headline = clickbait_lines[clickbait_type]
        print(headline)
    print()

    website = random.choice([
        'wobsite', 'blag', 'Facebuuk', 'Googles', 'Facesbook', 'Tweedie', 'Pastagram'
    ])

    when = random.choice(WHEN).lower()
    print(f'Post these to our {website} or you are fired!')


# Each of these functions returns a different type of headline
def generateAreMillennialsKillingHeadline():
    noun = random.choice(NOUNS)
    return f'Are Millennials Killing the {noun} Industy?'


def generateWhatYouDontKnowHeadline():
    noun = random.choice(NOUNS)
    plural_noun = random.choice(NOUNS) + 's'
    when = random.choice(WHEN)
    return f'Without this {noun}, {plural_noun} Could Kill You {when}.'


def generateBigCompaniesHateHerHeadline():
    pronoun = random.choice(OBJECTIVE_PRONOUNS)
    state = random.choice(STATES)
    noun1 = random.choice(NOUNS)
    noun2 = random.choice(NOUNS)
    return f'Big Companies Hate {pronoun}! See How This {state} {noun1} Invented a Cheaper {noun2}'


def generateYouWontBelieveHeadline():
    state = random.choice(STATES)
    noun = random.choice(NOUNS)
    pronoun = random.choice(POSSESSIVE_PRONOUNS)
    place = random.choice(PLACES)
    return f'You Wont Believe What This {state} {noun} Found in {pronoun} {place}'


def generateDontWantYouToKnowHeadline():
    plural_noun1 = random.choice(NOUNS) + 's'
    plural_noun2 = random.choice(NOUNS) + 's'
    return f'What {plural_noun1} Dont What You To Know About {plural_noun2}'


def generateGiftIdeaHeadline():
    number = random.randint(7, 15)
    noun = random.choice(NOUNS)
    state = random.choice(STATES)
    return f'{number} Gift Ideas to Give Your {noun} From {state}.'


def generateReasonsWhyHeadline():
    number1 = random.randint(3, 19)
    plural_noun = random.choice(NOUNS) + 's'
    # number2 should be no larger than number1
    number2 = random.randint(1, number1)
    return f'{number1} Reasons Why {plural_noun} Are More Interesting Than You Think (Number {number2} Will Surprise You!'


def generateJobAutomatedHeadline():
    state = random.choice(STATES)
    noun = random.choice(NOUNS)

    i = random.randint(0, 2)
    pronoun1 = POSSESSIVE_PRONOUNS[i]
    pronoun2 = PERSONAL_PRONOUNS[i]

    if pronoun1 == 'Their':
        return f'This {state} {noun} Didn\'t Think Robots Would Take {pronoun1} Job. {pronoun2} Were Wrong!'
    else:
        return f'This {state} {noun} Didn\'t Think Robots Would Take {pronoun1} Job. {pronoun2} Was Wrong!'


if __name__ == '__main__':
    main()
