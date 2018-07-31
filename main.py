import discord
import asyncio
from discord.ext.commands import Bot

bot = Bot(command_prefix=('!', '?'), description='A bot that sends messages to individual people and channels'
                                                 ' about news.')


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')



with open('token.txt', 'r') as file:
    bot.run(file.readline())
