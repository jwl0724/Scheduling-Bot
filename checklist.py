import csv
import helpers
import proper_usage


async def checklist_commands(message, command):    
    if not proper_usage.checklist(message.content, command):
        await message.channel.send('Error, invalid usage. Please use !help to see proper usage')
        return
    
    checklist_file = open('./storage/checklist.csv', 'r+', newline='')
    checklist_data = csv.DictReader(checklist_file)
    fields = ['author', 'content']
    author_tasks = [item for item in checklist_data if int(item['author']) == message.author.id]

    match command:
        case 'add':
            new_task = {'author': message.author.id, 'content': message.content.split('\'')[1]}
            writer = csv.DictWriter(checklist_file, fieldnames = fields)
            writer.__str__()
            writer.writerow(new_task)

            await message.channel.send('Task Added!')

        case 'finish':
            pass

        case 'remove':
            pass

        case 'clear':
            pass

        case 'checklist':
            formatted_string, index = '', 0

            for task in author_tasks:
                index += 1
                content = task['content']
                formatted_string += f'{index}. {content}\n'
                
            await message.channel.send(formatted_string)

    checklist_file.close()
    # csv file -> author,entry number,content