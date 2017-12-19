# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field


class GycrawlItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


# 废旧网数据#--
class FeiJiuItem(scrapy.Item):
    source = Field()                #报价来源
    branch = Field()                #牌号
    manufacturer = Field()          #厂商
    price = Field()                 #报价
    productName = Field()           #品名
