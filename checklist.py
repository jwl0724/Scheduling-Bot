import csv

def checklist_commands(message, command):
    checklist_file = open('./storage/checklist.csv', 'r+', newline='')
    checklist_data = csv.DictReader(checklist_file)
    author_posts = [item for item in checklist_data if int(item['author']) == message.author.id]

    match command:
        case 'add':
            pass

        case 'finish':
            pass

        case 'remove':
            pass

        case 'clear':
            pass

        case 'checklist':
            pass

        case _:
            message.channel.send('Error, invalid usage. Please use !help to see proper usage')

    checklist_file.close()
    # csv file -> author,entry number,content