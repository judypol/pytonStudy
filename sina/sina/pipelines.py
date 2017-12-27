# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from settings import MONGODB
import pymongo


class SinaPipeline(object):
    collection_name = 'hq'
    db_name = "sina"

    def __init__(self):
        self.host = MONGODB.get('host')
        self.port = MONGODB.get('port')

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(host=self.host, port=self.port)
        self.db = self.client[self.db_name]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        oldDateAndTime=self.db[self.collection_name].find_one({"name":item['name'],"time":item['time'],"date":item['date']})
        if not oldDateAndTime:
            self.db[self.collection_name].insert_one(dict(item))
        return item
