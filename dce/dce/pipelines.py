# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import settings


class DcePipeline(object):
    collection_night_name = 'dceNight'
    collection_day_name = 'dceDay'
    collection_member_name = 'dceMember'
    collection_week_name = 'dceWeek'
    collection_month_name = 'dceMonth'
    db_name = "dce"

    def __init__(self):
        self.host = settings.MONGODB.get('host')
        self.port = settings.MONGODB.get('port')

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(host=self.host, port=self.port)
        self.db = self.client[self.db_name]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        if spider.name == "dce_night":  # 保存到dceNight表中
            self.db[self.collection_night_name].insert_one(dict(item))
        elif spider.name == "dceDay":  # 保存到dceDay表中
            self.db[self.collection_day_name].insert_one(dict(item))
        elif spider.name == 'dceMember':  # 会员信息
            self.db[self.collection_member_name].insert_one(dict(item))
        elif spider.name == 'dceWeek':      #周行情
            self.db[self.collection_week_name].insert_one(dict(item))
        elif spider.name == 'dceMonth':     #月行情
            self.db[self.collection_month_name].insert_one(dict(item))

        return item
