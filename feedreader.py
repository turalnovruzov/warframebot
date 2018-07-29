import urllib3
import json


class FeedReader:
    def __init__(self, feed='http://content.warframe.com/dynamic/worldState.php'):
        self.http = urllib3.PoolManager()
        self.feed = feed

    async def read(self):
        res = self.http.request('GET', self.feed)
        if res.status != 200:
            raise Exception('Status not 200.')
        return json.loads(res.data)
