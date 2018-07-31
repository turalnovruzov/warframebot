from feedreader import FeedReader
from notifier import Notifier
from discord.ext.commands import Bot


class Updater:
    def __init__(self):
        self.interval = 5

    async def loop(self, bot: Bot, feedreader: FeedReader, notifier: Notifier):
        pass
