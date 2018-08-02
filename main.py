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
        await asyncio.wait([db_context.save_user_ids(ctx.message.author.id),
                     bot.say('{}, You are subscribed to the feed now!'.format(ctx.message.author.mention))])
    else:
        await bot.say('{}, You are already subscribed, to unsubscribe type **!unsubscribe**.'
                      .format(ctx.message.author.mention))


@bot.command(pass_context=True)
async def subscribe_channel(ctx):
    if ctx.message.author.server_permissions.administrator:
        channel_ids = await db_context.read_channel_ids()
        if ctx.message.channel.id not in channel_ids:
            await asyncio.wait([db_context.save_channel_ids(ctx.message.channel.id),
                          bot.say('{}, This channel is subscribed to the feed now!'.format(ctx.message.author.mention))])
        else:
            await bot.say('{}, This channel is already subscribed, to unsubscribe type **!unsubscribe**.'
                          .format(ctx.message.author.mention))



with open('token.txt', 'r') as file:
    token = file.readline()
    bot.run(token, loop=loop)


