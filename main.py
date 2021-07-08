import discord
import os

from discord import channel
from discord.activity import Game

if __name__ == "__main__":

    list_sad_words = ['sad', 'depressed', 'blue', 'down', 'heartbroken', 'mourn', 'somber', 'grief', 'hopelessness', 'unhappy']

    client = discord.Client()

    def help_display(message):

        return 'Try\n$hi - for a hello\n$fox - for a ascii fox\n$help - for list of commands'

    @client.event
    async def on_ready():
        print('I have logged in as {0.user}'.format(client))

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        if message.content.startswith('$hi'):
            guy = message.author.display_name
            await message.channel.send(f'~ hi {guy} ~')

        # if message.content.startswith('$fox'):
        #     await message.channel.send('~^｡^~')

        if message.content.startswith('$help'):
            await message.channel.send(help_display(message))

        if 'fox' in message.content:
            await message.channel.send('~ Are my ears burning? ~')
        
        if 'plans' in message.content:
            await message.channel.send("~ I'm free all afternoon! ~")

        for word in list_sad_words:
            if word in message.content.lower():
                await message.channel.send(f'~ Hey, I heard your feelin {word}. ~\n~ Hope your doin ok {message.author.display_name}. ~')
                # print(word)

            


    client.run('ODYwNzI5NTYxODc5Njc0ODgw.YN_e3w.Np38Rz3RbKavywIWWNYOx61CMAI')