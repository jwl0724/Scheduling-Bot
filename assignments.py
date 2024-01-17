import discord
import helpers
import csv
import re


FIELDS = ('author', 'deadline', 'assignment')


def retrieve_assignments(author_id):
    helpers.get_file_path(author_id, 'assignments')
    with open(f'./storage/assignments/{author_id}_assignments.csv', 'r') as file:
        file_reader = csv.DictReader(file, fieldnames=FIELDS)
        assignments = [assignment for assignment in file_reader if int(assignment['author']) == author_id]
    return assignments


def save_assignment(author_id, deadline, assignment):
    helpers.get_file_path(author_id, 'assignments')
    with open(f'./storage/assignments/{author_id}_assignments.csv', 'a', newline='') as file:
        file_writer = csv.DictWriter(file, fieldnames=FIELDS)
        entry = {'author': author_id, 'deadline': deadline, 'assignment': assignment}
        file_writer.__str__()
        file_writer.writerow(entry)


def delete_assignment(author_id, entry_no):
    pass


async def process_assignment_commands(message, command):
    match command:
        case 'save':
            regex_eval = re.search("!save [0-9][0-9]/20[0-9][0-9] '[a-zA-Z]+'", message.content)
            if not regex_eval:
                await message.channel.send('Invalid format, please see !help to see required format.')
                return
            deadline = re.search('[0-9][0-9]/20[0-9][0-9]', message.content).group()
            assignment = re.search("'[a-zA-Z]+'", message.content).group()
            save_assignment(message.author.id, deadline, assignment)
            await message.channel.send('Assignment saved!')

        case 'assignments':
            regex_eval = re.search('!assignments')
            if not regex_eval:
                await message.channel.send('Invalid format, please see !help to see required format.')
                return
            assignments = retrieve_assignments(message.author.id)
            await message.channel.send(assignments)

        case 'delete':
            regex_eval = re.search('!delete #[0-9]+', message.content)
            if not regex_eval:
                await message.channel.send('Invalid format, please see !help to see required format.')
                return
            
            entry_no = re.search('[0-9]+', message.content).group()

        case _:
            await message.channel.send('Invalid command. Please try again.')
