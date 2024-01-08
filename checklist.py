import csv
import helpers as help
import re


FIELDS = ('author', 'content', 'completion')


def add_task(author_id, task):
    cleaned_task = task.replace("'", '')
    with open('./storage/checklist.csv', 'a', newline='') as file:
        file_writer = csv.DictWriter(file, fieldnames=FIELDS)
        entry = {'author': author_id, 'content': cleaned_task, 'completion': False}
        file_writer.__str__()
        file_writer.writerow(entry)


def retrieve_checklist(author_id):
    with open('./storage/checklist.csv', 'r') as file:
        file_reader = csv.DictReader(file, fieldnames=FIELDS)
        tasks = [task for task in file_reader if int(task['author']) == author_id]
    return tasks


def get_task(author_id, entry_no):
    task_list = retrieve_checklist(author_id)
    try:
        return task_list[int(entry_no) - 1]
    except IndexError:
        return None
    except TypeError:
        return None


def edit_lines(author_id, specification=None, new_content=None):
    with open('./storage/checklist.csv', 'r', newline='') as file:
        file_reader = csv.DictReader(file, fieldnames=FIELDS)
        file_data = list(file_reader)
    
    with open('./storage/checklist.csv', 'w', newline='') as file:
        file_writer = csv.DictWriter(file, fieldnames=FIELDS)
        # rewrite lines not matching the selected for deletion
        for line in file_data:
            if int(line['author']) != author_id:
                file_writer.writerow(line)
                continue
            
            if line['content'] == specification:
                if new_content:
                    file_writer.writerow(new_content)

            elif specification:
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
            regex_eval = re.search('!finish #[0-9]+', message.content)
            if not regex_eval:
                await message.channel.send('Invalid format, please precede the entry number with #.')
                return
            
            entry_no = re.search('[0-9]+', message.content).group()
            finished_task = get_task(message.author.id, entry_no)
            if not finished_task:
                await message.channel.send('Error, please input a valid number.')
                return

            finished_task['completion'] = True
            edit_lines(message.author.id, specification=finished_task['content'], new_content=finished_task)
            await message.channel.send('Tasked Crossed Out!')

        case 'remove':
            regex_eval = re.search("!remove #[0-9]+", message.content)
            if not regex_eval:
                await message.channel.send('Invalid format, please precede the entry number with #.')
                return
            entry_no = re.search('[0-9]+', message.content).group()
            to_remove = get_task(message.author.id, entry_no)
            if not to_remove:
                await message.channel.send('Error, please input a valid number.')
                return
            
            edit_lines(message.author.id, specification=to_remove['content'])

        case 'clear':
            edit_lines(message.author.id)
            await message.channel.send('All tasks cleared!')

        case 'checklist':
            tasks = retrieve_checklist(message.author.id)
            if not tasks:
                await message.channel.send('No tasks found.')
                return
            
            formatted_string = ''
            for number, task in enumerate(tasks, 1):
                formatted_string += f'{number}. {task["content"]}\n' if not eval(task['completion']) else f'~~{number}. {task["content"]}~~\n' 

            await message.channel.send(formatted_string)
