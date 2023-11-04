import helpers

def checklist(message_content, command):
    stripped_message = message_content.strip()

    if stripped_message == '!checklist' or stripped_message == '!clear': return True

    elif command == 'remove' or command == 'finish':
        try:
            if stripped_message[8] == '#' and helpers.get_entry_number(stripped_message): return True
        except:
            return False
    
    else:
        try:
            if stripped_message[5] == '\'' and stripped_message[-1] == '\'': return True
        except IndexError:
            return False
        