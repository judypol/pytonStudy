# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field


class HexunItem(scrapy.Item):
    # define the fields for your item here like:
    product=Field()     #产品
    dateTime = Field()  # 时间
    price = Field()  # 价格
    amount = Field()  # 成交额
    volumn = Field()  # 成交量
    avePrice = Field()  # 领先指标
    openInterest = Field()  # 持仓量
