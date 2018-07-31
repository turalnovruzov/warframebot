import discord
from discord.ext.commands import Bot


class Notifier:
    def __init__(self, bot: Bot):
        self._bot = bot

    async def notify(self, user_ids, channel_ids):
        pass

    async def notify_users(self, user_ids):
        """
        Notifies all the given Users about the news

        :param user_ids:
        Id of the users

        :return:
        None
        """
        pass

    async def notify_channels(self, channel_ids):
        """
        Notifies all the given Channels about the news

        :param channel_ids:
        Id of the channels

        :return:
        None
        """
        pass
