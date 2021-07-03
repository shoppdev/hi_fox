import discord
import os

if __name__ == "__main__":

    client = discord.Client()

    @client.event
    async def on_ready():
        print('We have logged in as {0.user}'.format(client))

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        if message.content.startswith('$hi'):
            guy = message.author
            await message.channel.send(f'hi {guy}')

        if message.content.startswith('$fox'):
            await message.channel.send('ｰ^｡^ｰ')

    client.run('')