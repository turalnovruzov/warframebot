import discord
import datetime
import time


class EmbedGenerator:
    @staticmethod
    async def embed_event(event):
        title = ''
        for message in event['Messages']:
            if message['LanguageCode'] == 'en':
                title = message['Message']
                break
        embed = discord.Embed(title=title,
                              url=event['Prop'],
                              timestamp=datetime.datetime.fromtimestamp(time.time()))
        embed.set_image(url='https://n9e5v4d8.ssl.hwcdn.net/uploads/b46930e89ac11d80be36ff35e3c299ef.jpg')
        return embed
