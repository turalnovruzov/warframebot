import asyncio
import pickle
import mysql.connector
import os


class DbContext:
    def __init__(self, host, username, password):
        self.db = mysql.connector.connect(
            host=host,
            user=username,
            passwd=password,
            database='warframebot'
        )
        self.folder = 'data/'
        self.feed = self.folder + 'feed.pkl'
        self.lock_sql = asyncio.Lock()
        self.lock_os = asyncio.Lock()

    async def save_feed(self, feed):
        """
        Truncates the current feed and saves the given one.

        :param feed:
        The feed that is going to be saved

        :return:
        None
        """
        try:
            async with self.lock_os:
                with open(self.feed, 'w') as file:
                    pickle.dump(feed, file)
        except FileNotFoundError:
            if not os.path.isdir(self.folder):
                os.mkdir(self.folder)
            open(self.feed, 'w').close()

    async def save_user_ids(self, *ids):
        """
        Saves the Ids

        :param ids:
        Id of the users

        :return:
        None
        """
        async with self.lock_sql:
            if len(ids) > 0:
                _ids = []
                for i in ids:
                    _ids.append((i,))
                cursor = self.db.cursor()
                cursor.executemany('INSERT INTO user (discord_id) VALUES (%s)', _ids)
                self.db.commit()

    async def save_channel_ids(self, *ids):
        """
        Saves the Ids

        :param ids:
        Id of the channels

        :return:
        None
        """
        async with self.lock_sql:
            if len(ids) > 0:
                _ids = []
                for i in ids:
                    _ids.append((i,))
                cursor = self.db.cursor()
                cursor.executemany('INSERT INTO channel (discord_id) VALUES (%s)', _ids)
                self.db.commit()

    async def read_feed(self):
        """
        Read saved feed

        :return:
        The feed as python object objects
        """
        try:
            async with self.lock_os:
                with open(self.feed, 'r') as file:
                    return pickle.load(file)
        except FileNotFoundError:
            if not os.path.isdir(self.folder):
                os.mkdir(self.folder)
            open(self.feed, 'w').close()

    async def read_user_ids(self):
        """
        Reads saved Ids of the users

        :return:
        The Ids as a list of strings
        """
        async with self.lock_sql:
            cursor = self.db.cursor()
            cursor.execute('SELECT discord_id FROM user')
            return cursor.fetchall()[0][0]

    async def read_channel_ids(self):
        """
        Reads saved Ids of the channels

        :return:
        The Ids as a list of strings
        """
        async with self.lock_sql:
            cursor = self.db.cursor()
            cursor.execute('SELECT discord_id FROM channel')
            return cursor.fetchall()[0][0]
