import datetime

DAYS = (
    'Sunday',
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday',
)

MONTHS = (
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December',
)

# get a year from the user
while True:
    print('Enter the year for calendar:')
    response = input('> ')

    if response.isdecimal() and int(response) > 0:
        year = int(response)
        break
    
    print('Please enter a numeric year, like 2024')
    continue


# get a month from the user
while True:
    print('Enter the month for the calendar, 1-12')
    response = input('> ')

    # response true if str.isdecimal('numeric')
    if not response.isdecimal():
        print('Please enter a numeric month, like 3 for March')
        continue
    
    month = int(response)
    if 1 <= month <= 12:
        break
    
    print('Please enter a number from 1 to 12')


def get_calendar_for(year, month):
    # contains string of the calendar
    calendar_text = ''

    # put the month and year at the top of the calendar
    calendar_text += f"{(' ' * 34)}{MONTHS[month-1]} {str(year)}\n"

    # add the days of the week labels to the calendar
    days_of_week = ''.join((f'....{day}' for day in DAYS))
    calendar_text += f'{days_of_week}..\n'

    # the horizontal line string that separates weeks
    week_separator = f"{('+----------' * 7)}+\n"

    # the blank rows have the 10 spaces in between the | day separaotrs
    blank_row = f"{('|          ' * 7)}|\n"

    # get the first date in the month
    current_date = datetime.date(year=year, month=month, day=1) # YYYY-MM-DD

    # roll back current_date until it is Sunday
    # weekday() returns 6 for Sunday not 0 for Monday
    while current_date.weekday() != 6:
        current_date -= datetime.timedelta(days=1)

    # loop over each week in a month
    while True:
        calendar_text += week_separator

        # day_number_row is the row with the day number labels
        day_number_row = ''

        for _ in range(7):
            day_number_label = str(current_date.day).rjust(2)
            day_number_row += f"|{day_number_label}{(' ' * 8)}"
            # go to the next day
            current_date += datetime.timedelta(days=1)
        
        day_number_row += '|\n'

        # add the day row and 3 blanks rows to the calendar text
        calendar_text += day_number_row

        for _ in range(3):
            calendar_text += blank_row

        # check if we're done with the month
        if current_date.month != month:
            break

    
    # add the horizontal line at the very bottom of the calendar
    calendar_text += week_separator
    return calendar_text


calendar_text = get_calendar_for(year=year, month=month)
print(calendar_text)

# save the calendar to a file
calendar_filename = f'calendar_{year}_{month}.txt'
with open(calendar_filename, 'w') as file:
    file.write(calendar_text)

print(f'Saved to {calendar_filename}')







