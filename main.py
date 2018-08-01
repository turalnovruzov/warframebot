import asyncio
from notifier import Notifier
from dbcontext import DbContext
from updater import Updater
from feedreader import FeedReader
from discord.ext.commands import Bot, Context

loop = asyncio.get_event_loop()
lock = asyncio.Lock()
bot = Bot(command_prefix=('!'), description='A bot that sends messages to individual people and channels'
                                                 ' about news.')
db_context = DbContext(lock)
notifier = Notifier(bot)
updater = Updater()
feed_reader = FeedReader()


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    loop.create_task(updater.loop(loop, bot, feed_reader, notifier, db_context))


@bot.command(pass_context=True)
async def subscribe(ctx):
    user_ids = await db_context.read_user_ids()
    if ctx.message.author.id not in user_ids:
        await db_context.save_user_ids(ctx.message.author.id)
        await bot.say('{}, You are subscribed to the feed now!'.format(ctx.message.author.mention))
    else:
        await bot.say('{}, You are already subscribed, to unsubscribe type **!unsubscribe**.'
                      .format(ctx.message.author.mention))

with open('token.txt', 'r') as file:
    token = file.readline()
    bot.run(token, loop=loop)


