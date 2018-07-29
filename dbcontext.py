import pickle


class DbContext:
    def __init__(self):
        self._feed = 'feed.pkl'
        self._user_ids = 'user_ids.dat'
        self._channel_ids = 'channel_ids.dat'

    def save_feed(self, feed):
        """
        Truncates the current feed and saves the given one.

        :param feed:
        The feed that is going to be saved

        :return:
        None
        """
        try:
            with open(self._feed, 'w+') as file:
                pickle.dump(feed, file)
        except Exception as ex:
            print(ex)

    def save_user_ids(self, *_ids):
        """
        Saves the Ids

        :param _ids:
        Id of the users

        :return:
        None
        """
        try:
            with open(self._user_ids, 'a+') as file:
                file.writelines(_ids)
        except Exception as ex:
            print(ex)

    def save_channel_ids(self, *_ids):
        """
        Saves the Ids

        :param _ids:
        Id of the channels

        :return:
        None
        """
        try:
            with open(self._channel_ids, 'a+') as file:
                file.writelines(_ids)
        except Exception as ex:
            print(ex)

    def read_feed(self):
        """
        Read saved feed

        :return:
        The feed as python object objects
        """
        try:
            with open(self._feed, 'r+') as file:
                return pickle.load(file)
        except Exception as ex:
            print(ex)

    def read_user_ids(self):
        """
        Reads saved Ids of the users

        :return:
        The Ids as a list of strings
        """
        try:
            with open(self._user_ids, 'r+') as file:
                return [line.rstrip('\n') for line in file]
        except Exception as ex:
            print(ex)

    def read_channel_ids(self):
        """
        Reads saved Ids of the channels

        :return:
        The Ids as a list of strings
        """
        try:
            with open(self._channel_ids, 'r+') as file:
                return [line.rstrip('\n') for line in file]
        except Exception as ex:
            print(ex)
