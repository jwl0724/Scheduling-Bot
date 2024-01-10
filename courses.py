import helpers as help
import requests
import discord
import os
import re


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
            
            
        case 'courses':
            pass
        case 'update':
            pass