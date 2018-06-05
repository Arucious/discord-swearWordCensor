import discord
import asyncio
from discord.ext.commands import Bot

Client = discord.Client()
client = Bot(command_prefix="!")

f = open("swear_words.txt") # list of swear words 
curses = f.read().splitlines() # make list of words

@client.event
async def on_ready(): # start of the bot 
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if any(word in message.content.lower() for word in curses):
        return await client.send_message(message.channel,"CURSING NOT ALLOWED")

client.run() #put API key ID here in between quotes
