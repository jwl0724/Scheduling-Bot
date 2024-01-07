import csv
import helpers as help
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


def get_task(author_id, entry_no):
    task_list = retrieve_checklist(author_id)
    try:
        return task_list[entry_no - 1]
    except IndexError:
        return None


def finish_task(author_id, finished_task):  
    with open('./storage/checklist.csv', 'a+', newline='') as file:
        file.seek(0)
        file_reader = csv.DictReader(file, fieldnames=FIELDS)
        for line in file_reader:
            if int(line['author']) == author_id and line['content'] == finished_task:
                file.write(f'{author_id},~~{finished_task}~~')




def clear_tasks(author_id):
    with open('./storage/checklist.csv', 'r', newline='') as read_file:
        file_reader = csv.DictReader(read_file, fieldnames=FIELDS)
        file_data = list(file_reader)

    with open('./storage/checklist.csv', 'w', newline='') as write_file:
        file_writer = csv.DictWriter(write_file, fieldnames=FIELDS)

        # rewrite lines that do not belong to the author
        for line in file_data:
            if int(line['author']) != author_id:
                file_writer.writerow(line)


async def process_checklist_commands(message, command):    
    match command:
        case 'add':
            regex_eval = re.search("!add '.+'", message.content)
            if not regex_eval:
                await message.channel.send('Invalid format, please wrap your task in single quotes.')
                return
            
            new_task = re.search("'.+'", message.content).group()
            add_task(message.author.id, new_task)
            await message.channel.send('Task Added!')

        case 'finish':
            regex_eval = re.search('!finish #[0-9]+')
            if not regex_eval:
                await message.channel.send('Invalid format, please precede the entry number with #.')
                return
            
            entry_no = re.search('[0-9]+', message.content).group()
            finished_task = get_task(message.author.id, entry_no)
            if not finished_task:
                await message.channel.send('The entry number you put in doesn\'t exist, please put a valid number.')
                return

            finish_task(message.author.id, finished_task)
            await message.channel.send('Tasked Crossed Out!')

        case 'remove':
            pass

        case 'clear':
            clear_tasks(message.author.id)
            await message.channel.send('All tasks cleared!')

        case 'checklist':
            tasks = retrieve_checklist(message.author.id)
            if not tasks:
                await message.channel.send('No tasks found.')
                return
            
            formatted_string = ''
            for number, task in enumerate(tasks, 1):
                formatted_string += f'{number}. {task}\n'

            await message.channel.send(formatted_string)
