import asyncio
import discord
from discord.ext.commands import Bot


class Notifier:
    def __init__(self, bot: Bot):
        self.bot = bot

    async def notify(self, user_ids, channel_ids, content=None, embed=None):
        """
        Notifies all the given Users and Channels with the given content

        :param content:
        Content that is going to be notified

        :param embed:
        A discord.Embed object

        :param user_ids:
        Id of the users

        :param channel_ids:
        Id of the channels

        :return:
        None
        """
        await asyncio.wait([self.notify_users(content, embed, user_ids),
                            self.notify_channels(content, embed, channel_ids)])

    async def notify_users(self, content, embed, user_ids):
        """
        Notifies users with the given ids

        :param content:
        Content that is going to be notified

        :param embed:
        A discord.Embed object

        :param user_ids:
        Id of the users

        :return:
        None
        """
        messages = []
        for _id in user_ids:
            user = discord.utils.find(lambda x: x.id == _id, self.bot.get_all_members())
            if user is not None:
                messages.append(self.bot.send_message(user, content=content, embed=embed))
            if len(messages) != 0:
                await asyncio.wait(messages)

    async def notify_channels(self, content, embed, channel_ids):
        """
        Notifies channels with the given ids

        :param content:
        Content that is going to be notified

        :param embed:
        A discord.Embed object

        :param channel_ids:
        Id of the channels

        :return:
        List of coroutines
        """
        messages = []
        for _id in channel_ids:
            channel = self.bot.get_channel(_id)
            if channel is not None:
                messages.append(self.bot.send_message(channel, content=content, embed=embed))
        if len(messages) != 0:
            await asyncio.wait(messages)
