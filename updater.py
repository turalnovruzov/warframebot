from feedreader import FeedReader
from notifier import Notifier
from dbcontext import DbContext
from discord.ext.commands import Bot
import asyncio


class Updater:
    def __init__(self):
        self.interval = 5

    async def loop(self, loop, bot: Bot, feed_reader: FeedReader, notifier: Notifier, db_context: DbContext):
        await db_context.read_user_ids()
