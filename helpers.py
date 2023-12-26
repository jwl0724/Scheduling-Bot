def get_entry_number(message_content):
    try:
        convert_to_int = int(message_content[9:])
        return convert_to_int
    except ValueError:
        return 0
    

def get_command(message_content):
    command = message_content[1:].lower().split()[0]
    return command