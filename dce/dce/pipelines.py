# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from settings import MONGODB


class DcePipeline(object):
    collection_name = 'dce'
    db_name = "nightQuotes"

    def __init__(self):
        self.host = MONGODB.get('host')
        self.port = MONGODB.get('port')

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(host=self.host, port=self.port)
        self.db = self.client[self.db_name]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        if spider.name != "dce_night":
            return item

        self.db[self.collection_name].insert_one(dict(item))
        return item
    
