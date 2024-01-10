import helpers as help
from PIL import Image
import requests
import discord
import os
import io
import re


def delete_image(author_id):
    folder_path = help.get_file_path(author_id, 'schedule')
    to_delete = os.path.join(folder_path, os.listdir(folder_path)[0]) # Folder will always only have 1 file
    os.remove(to_delete)


def save_image(author_id, img_url, file_type):
    folder_path = help.get_file_path(author_id, 'schedule')
    if len(os.listdir(folder_path)) > 0:
        delete_image(author_id)
    file_path = os.path.join(folder_path, f"schedule.{file_type.replace('image/', '')}") 
    image_data = requests.get(img_url).content
    image = Image.open(io.BytesIO(image_data))
    image.save(file_path)


async def process_course_commands(message, command):
    match command:
        case 'schedule':
            if not len(message.attachments):
                await message.channel.send('Please upload an image of your schedule')
                return
            if len(message.attachments) > 1:
                await message.channel.send('Please upload 1 image at a time')
                return
            if 'image' not in message.attachments[0].content_type:
                await message.channel.send('Please upload an image file')
                return
            save_image(message.author.id, message.attachments[0].url, message.attachments[0].content_type)
            await message.channel.send('Image has been received and saved!')
            
        case 'courses':
            schedule_folder = help.get_file_path(message.author.id, 'schedule')
            if not len(os.listdir(schedule_folder)):
                await message.channel.send('No schedule found in storage')
                return
            schedule_image = os.path.join(schedule_folder, os.listdir(schedule_folder)[0])
            img_file = discord.File(schedule_image)
            await message.channel.send(content='Here is your schedule', file=img_file)

        case 'drop':
            schedule_folder = help.get_file_path(message.author.id, 'schedule')
            if not len(os.listdir(schedule_folder)):
                await message.channel.send('No schedule to delete')
                return
            delete_image(message.author.id)
            await message.channel.send('Course schedule was been successfully deleted!')