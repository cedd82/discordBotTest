#  with Python 3.8
import discord
from discord.ext import commands
import random

TOKEN = ''

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return
        print(message)
        await message.channel.send('Hello {0.author.mention}'.format(message))
        print('sent')

client = MyClient()
client.run(TOKEN)
