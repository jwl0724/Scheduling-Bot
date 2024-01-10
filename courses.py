import helpers as help
from PIL import Image
import requests
import discord
import os
import io
import re


def save_image(author_id, img_url, file_type):
    folder_path = help.get_file_path(author_id, 'schedule')
    if len(os.listdir(folder_path)) > 0:
        to_delete = os.path.join(folder_path, os.listdir(folder_path)[0])
        os.remove(to_delete)
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
            pass
        case 'update':
            pass