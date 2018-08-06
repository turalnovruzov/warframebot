import asyncio
import pickle
import mysql.connector
import os
import itertools


class DbContext:
    def __init__(self, host, username, password):
        self.db = mysql.connector.connect(
            host=host,
            user=username,
            passwd=password,
            database='warframebot'
        )
        self.folder = './data/'
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
                with open(self.feed, 'wb') as file:
                    pickle.dump(feed, file)
        except FileNotFoundError:
            os.mkdir(self.folder)
            with open(self.feed, 'wb') as file:
                pickle.dump(feed, file)

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
                with open(self.feed, 'rb') as file:
                    s = pickle.load(file)
                    return s
        except FileNotFoundError:
            if not os.path.isdir(self.folder):
                os.mkdir(self.folder)
            open(self.feed, 'w').close()
        except EOFError:
            pass
        finally:
            return None

    async def read_user_ids(self):
        """
        Reads saved Ids of the users

        :return:
        The Ids as a list of strings
        """
        async with self.lock_sql:
            cursor = self.db.cursor()
            cursor.execute('SELECT discord_id FROM user')
            return itertools.chain.from_iterable(cursor.fetchall())

    async def read_channel_ids(self):
        """
        Reads saved Ids of the channels

        :return:
        The Ids as a list of strings
        """
        async with self.lock_sql:
            cursor = self.db.cursor()
            cursor.execute('SELECT discord_id FROM channel')
            return itertools.chain.from_iterable(cursor.fetchall())

    async def user_exists(self, _id):
        """
        Checks if the given user id is saved in the database

        :param _id:
        Id to be checked

        :return:
        True if exists, False otherwise
        """
        async with self.lock_sql:
            cursor = self.db.cursor()
            cursor.execute('SELECT discord_id FROM user WHERE discord_id=%s', (_id,))
            if len(cursor.fetchall()) > 0:
                return True
            else:
                return False

    async def channel_exists(self, _id):
        """
        Checks if the given channel id is saved in the database

        :param _id:
        Id to be checked

        :return:
        True if exists, False otherwise
        """
        async with self.lock_sql:
            cursor = self.db.cursor()
            cursor.execute('SELECT discord_id FROM channel WHERE discord_id=%s', (_id,))
            if len(cursor.fetchall()) > 0:
                return True
            else:
                return False

    async def delete_user_id(self, *ids):
        """
        Deletes the given user id from database

        :param id:
        User id to be deleted

        :return:
        None
        """
        if len(ids) > 0:
            _ids = []
            for i in ids:
                _ids.append((i,))
            cursor = self.db.cursor()
            cursor.executemany('DELETE FROM user WHERE discord_id=%s', _ids)
            self.db.commit()

    async def delete_channel_ids(self, *ids):
        """
        Deletes the given user id from database

        :param id:
        User id to be deleted

        :return:
        None
        """
        if len(ids) > 0:
            _ids = []
            for i in ids:
                _ids.append((i,))
            cursor = self.db.cursor()
            cursor.executemany('DELETE FROM channel WHERE discord_id=%s', _ids)
            self.db.commit()
