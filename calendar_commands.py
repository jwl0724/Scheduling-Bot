from datetime import date
import calendar


async def process_calendar_commands(message, command):
    current_year = date.today().year
    current_month = date.today().month
    match command:
        case 'calendar':
            await message.channel.send(f'{calendar.calendar(current_year)}')

        case 'today':
            month_key = {
                1: 'January', 2: 'February', 3: 'March', 
                4: 'April', 5: 'May', 6: 'June', 
                7: 'July', 8: 'August', 9: 'September',
                10: 'October', 11: 'November', 12: 'December'
            }
            await message.channel.send(f'Today is {month_key[current_month]} {date.today().day} {current_year}')

        case 'month':
            await message.channel.send(f'{calendar.month(current_year, current_month)}')