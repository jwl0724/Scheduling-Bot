import re
import requests
import os


def get_file_path(author_id):
    file_path = os.path.join(os.path.dirname(__file__), f'storage/{author_id}')
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    return file_path


def write_file(author_id, file_name, notes_url):
    file_path = get_file_path(author_id)
    response = requests.get(notes_url)
    joined_path = os.path.join(file_path, f'{author_id}_{file_name}')
    with open(joined_path, 'w') as file:
        notes_list = response.text.splitlines() # each line has extra /r/n, leading to extra spaces
        for note in notes_list:
            note += '\n'
            file.write(note)


async def process_notes_commands(message, command):
    match command:
        case 'upload':
            if not len(message.attachments):
                await message.channel.send('Please upload a .txt file.')
                return
            if len(message.attachments) > 1:
                await message.channel.send('Please upload 1 file at a time.')
                return
            if not re.search('[a-zA-Z0-9]+.txt', message.attachments[0].filename):
                await message.channel.send('The file you tried to upload is not a .txt file')
                return
            
            write_file(message.author.id, message.attachments[0].filename, message.attachments[0].url)

        case 'notes':
            pass
        case 'pull':
            pass
        case 'delete':
            pass
        case 'update':
            pass
