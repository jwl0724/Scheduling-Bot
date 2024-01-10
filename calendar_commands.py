from datetime import date
import calendar
import re


async def process_calendar_commands(message, command):
    current_year = date.today().year
    current_month = date.today().month
    match command:
        case 'calendar':
            await message.channel.send(f'{calendar.month(current_year, current_month)}')

        case 'today':
            month_key = {
                1: 'January', 2: 'February', 3: 'March', 
                4: 'April', 5: 'May', 6: 'June', 
                7: 'July', 8: 'August', 9: 'September',
                10: 'October', 11: 'November', 12: 'December'
            }
            await message.channel.send(f'Today is {month_key[current_month]} {date.today().day} {current_year}')

        case 'month':
            regex_eval = re.search('!month [a-zA-Z]+$', message.content.strip())
            if not regex_eval:
                await message.channel.send('Invalid format, please use !help to see proper usage of !month')
                return

            month_key = {
                'january': 1, 'jan': 1, 'february': 2, 'feb': 2, 'march': 3, 'mar': 3, 
                'april': 4, 'apr': 4, 'may': 5, 'june': 6, 'jun': 6, 'july': 7, 
                'jul': 7, 'august': 8, 'aug': 8, 'september': 9, 'sept': 9, 'sep': 9,
                'october': 10, 'oct': 10, 'november': 11, 'nov': 11, 'december': 12, 'dec': 12
            }
            month_input = message.content.lower().split(' ')[1]
            month = month_key.get(month_input)
            if not month:
                await message.channel.send('The month you inputted was not found')
                return
            await message.channel.send(f'{calendar.month(current_year, month)}')