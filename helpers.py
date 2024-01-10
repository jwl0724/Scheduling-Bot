import os

def get_entry_number(message_content):
    try:
        convert_to_int = int(message_content[9:])
        return convert_to_int
    except ValueError:
        return 0
    

def get_file_path(author_id, sub_folder, file_name=None):
    if file_name:
        sub_folder += f'/{file_name}'
    file_path = os.path.join(os.path.dirname(__file__), f'storage/{author_id}/{sub_folder}')
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    return file_path


def get_command(message_content):
    command = message_content[1:].lower().split()[0]
    return command