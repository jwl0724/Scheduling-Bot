import re
import requests
import os
import discord
import helpers as help


def get_notes(author_id):
    file_path = help.get_file_path(author_id, 'notes')
    if not len(os.listdir(file_path)):
        return None
    file_list = [file.replace(f'{author_id}_', '') for file in os.listdir(file_path)]
    return file_list


def get_selected_file(author_id, entry_no):
    notes_list = get_notes(author_id)
    if not notes_list:
        return None
    try:
        selected_note = notes_list[int(entry_no) - 1]
    except IndexError:
        return None
    except TypeError:
        return None
    
    return selected_note


def read_notes(author_id, file_name):
    file_path = help.get_file_path(author_id, 'notes')
    with open(os.path.join(file_path, f'{author_id}_{file_name}'), 'r') as file:
        data = file.readlines()
    return data


def write_file(author_id, file_name, notes_url):
    file_path = help.get_file_path(author_id, 'notes')
    response = requests.get(notes_url)
    joined_path = os.path.join(file_path, f'{author_id}_{file_name}')
    with open(joined_path, 'w') as file:
        notes_list = response.text.splitlines() # each line has extra /r/n, leading to extra spaces
        for note in notes_list:
            note += '\n'
            file.write(note)


def delete_file(author_id, file_name):
    file_path = help.get_file_path(author_id, 'notes')
    joined_path = os.path.join(file_path, f'{author_id}_{file_name}')
    os.remove(joined_path)


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
            await message.channel.send('File successfully uploaded!')

        case 'notes':
            notes_list = get_notes(message.author.id)
            if not notes_list:
                await message.channel.send('No note files found.')
                return
            
            formatted_string = ''
            for number, note in enumerate(notes_list, 1):
                formatted_string += f'{number}. {note}\n'
            await message.channel.send(formatted_string)

        case 'pull':
            regex_eval = re.search('!pull #[0-9]+', message.content)
            if not regex_eval:
                await message.channel.send('Invalid format, please see !help to see proper usage of pull')
                return
            file_name = get_selected_file(message.author.id, re.search('[0-9]+', message.content).group())
            if not file_name:
                await message.channel.send('Please input a valid entry number')
                return
            author_folder_path = help.get_file_path(message.author.id)
            internal_name = os.path.join(author_folder_path, f'{message.author.id}_{file_name}')
            external_name = os.path.join(author_folder_path, f'{file_name}')
            os.rename(internal_name, external_name)
            selected_file = discord.File(external_name)
            await message.channel.send(file=selected_file, content=f'{file_name} sent!')
            selected_file.close()
            os.rename(external_name, internal_name)

        case 'delete':
            regex_eval = re.search('!delete #[0-9]+', message.content)
            if not regex_eval:
                await message.channel.send('Invalid format, please see !help to see proper usage of delete')
                return
            file_name = get_selected_file(message.author.id, re.search('[0-9]+', message.content).group())
            if not file_name:
                await message.channel.send('Please input a valid entry number')
                return
            delete_file(message.author.id, file_name)
            await message.channel.send('File successfully removed from storage!')

        case 'view':
            regex_eval = re.search('!view #[0-9]+', message.content)
            if not regex_eval:
                await message.channel.send('Invalid format, please see !help for proper usage of view')
                return
            file_name = get_selected_file(message.author.id, re.search('[0-9]+', message.content).group())
            if not file_name:
                await message.channel.send('Please input a valid entry number')
                return
            notes = read_notes(message.author.id, file_name)
            formatted_string = f'**Reading from {file_name}**\n'.upper()
            for note in notes:
                formatted_string += f'{note}'
            await message.channel.send(formatted_string)
