import csv
import helpers as help
import proper_usage
import re


FIELDS = ('author', 'content')

def add_task(author_id, task):
    cleaned_task = task.replace("'", '')
    with open('./storage/checklist.csv', 'a', newline='') as file:
        file_writer = csv.DictWriter(file, fieldnames=FIELDS)
        entry = {'author': author_id, 'content': cleaned_task}
        file_writer.__str__()
        file_writer.writerow(entry)


def retrieve_checklist(author_id):
    with open('./storage/checklist.csv', 'r') as file:
        file_reader = csv.DictReader(file, fieldnames=FIELDS)
        tasks = [task['content'] for task in file_reader if int(task['author']) == author_id]
    return tasks


async def process_checklist_commands(message, command):    
    match command:
        case 'add':
            regex_eval = re.search("'.+'", message.content)
            if not regex_eval:
                await message.channel.send('Invalid format, please wrap your task in single quotes')
                return
            
            new_task = regex_eval.group()
            add_task(message.author.id, new_task)
            await message.channel.send('Task Added!')

        case 'finish':
            pass

        case 'remove':
            pass

        case 'clear':
            pass

        case 'checklist':
            tasks = retrieve_checklist(message.author.id)
            if not tasks:
                await message.channel.send('No tasks found.')
                return
            
            formatted_string = ''
            for number, task in enumerate(tasks, 1):
                formatted_string += f'{number}. {task}\n'

            await message.channel.send(formatted_string)


