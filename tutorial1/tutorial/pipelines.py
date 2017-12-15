# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from settings import MONGODB
from scrapy import log
import items
import pymongo


class MongoDBPipeline(object):
    def __init__(self):
        self._db = MONGODB.get('db')
        self._collection = MONGODB.get('collection')
        self._host = MONGODB.get('host')
        self._port = MONGODB.get('port')

        connection = pymongo.MongoClient(
            self._host, self._port
        )

        db = connection[self._collection]
        self.collection = db[self._db]

    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                raise items.DmozItem("Missing {0}!".format(data))
        if valid:
            self.collection.insert(dict(item))
            # log.msg("Question added to MongoDB database!",
            #         level=log.DEBUG, spider=spider)
        return item
