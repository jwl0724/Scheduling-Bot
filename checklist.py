def checklist_commands(message):
    # shave ! off of message
    command = message.content[1:].lower()
    action = command.split(' ')[0]
    
    try:
        operation = command.split(' ')[1]
        if '#' in operation:
            entry_num = int(operation[1:])

    except IndexError:
        pass
    except ValueError:
        message.channel.send('Error, # must be followed with a number')
        return

    # csv file -> author,entry number,content

    # switch case for different commands
    match action:
        case 'add':
            checklist = open('checklist.txt', 'w')
            entry = checklist.write(message.content)

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
        case _:
            message.channel.send('Error, invalid usage. Please use !help to see proper usage')
            return