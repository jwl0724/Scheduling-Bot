def checklist_commands(message):
    # shave ! off of message
    command = message.content[1:].lower()
    operation = command.split(' ')

    # switch case for different commands
    match operation:
        case 'add':
            # add stuff to list
            return
        case 'finish': 
            # strikethrough entry from list
            return
        case 'remove':
            # remove entry from list
            return
        case 'clear':
            # remove all entiries from list
            return