import pickle
import os


class DbContext:
    def __init__(self, lock):
        self.folder = 'data/'
        self.feed = self.folder + 'feed.pkl'
        self.user_ids = self.folder + 'user_ids.dat'
        self.channel_ids = self.folder + 'channel_ids.dat'
        self.lock = lock

    async def save_feed(self, feed):
        """
        Truncates the current feed and saves the given one.

        :param feed:
        The feed that is going to be saved

        :return:
        None
        """
        try:
            with open(self.feed, 'w') as file:
                pickle.dump(feed, file)
        except Exception as ex:
            print(ex)

    async def save_user_ids(self, *_ids):
        """
        Saves the Ids

        :param _ids:
        Id of the users

        :return:
        None
        """
        try:
            with open(self.user_ids, 'a') as file:
                file.writelines(_ids)
        except Exception as ex:
            print(ex)

    async def save_channel_ids(self, *_ids):
        """
        Saves the Ids

        :param _ids:
        Id of the channels

        :return:
        None
        """
        try:
            with open(self.channel_ids, 'a') as file:
                file.writelines(_ids)
        except Exception as ex:
            print(ex)

    async def read_feed(self):
        """
        Read saved feed

        :return:
        The feed as python object objects
        """
        try:
            with open(self.feed, 'r') as file:
                return pickle.load(file)
        except FileNotFoundError:
            if not os.path.isdir(self.folder):
                os.mkdir(self.folder)
            open(self.feed, 'w').close()
        except Exception as ex:
            print(ex)

        return []

    async def read_user_ids(self):
        """
        Reads saved Ids of the users

        :return:
        The Ids as a list of strings
        """
        try:
            with open(self.user_ids, 'r') as file:
                return [line.rstrip('\n') for line in file]
        except FileNotFoundError:
            if not os.path.isdir(self.folder):
                os.mkdir(self.folder)
            open(self.user_ids, 'w').close()
        except Exception as ex:
            print(ex)

        return []

    async def read_channel_ids(self):
        """
        Reads saved Ids of the channels

        :return:
        The Ids as a list of strings
        """
        try:
            with open(self.channel_ids, 'r') as file:
                return [line.rstrip('\n') for line in file]
        except FileNotFoundError:
            if not os.path.isdir(self.folder):
                os.mkdir(self.folder)
            open(self.channel_ids, 'w').close()
        except Exception as ex:
            print(ex)

        return []
