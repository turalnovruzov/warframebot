from src.feedreader import FeedReader
from src.notifier import Notifier
from src.dbcontext import DbContext
from discord.ext.commands import Bot
import asyncio


class Updater:
    def __init__(self):
        self.interval = 5

    async def loop(self, loop, bot: Bot, feed_reader: FeedReader, notifier: Notifier, db_context: DbContext):
        saved_feed, new_feed, user_ids, channel_ids = await asyncio.gather(db_context.read_feed(),
                                                                           feed_reader.read(),
                                                                           db_context.read_user_ids(),
                                                                           db_context.read_channel_ids())

        await db_context.save_feed('asdasd')
