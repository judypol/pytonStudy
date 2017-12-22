# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class SinaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()  # 名字
    time = scrapy.Field()  # 时间
    openPrice = scrapy.Field()  # 开盘价
    highestPrice = scrapy.Field()  # 最高价
    lowestPrice = scrapy.Field()  # 最低价
    yestodayClosePrice = scrapy.Field()  # 昨日收盘价
    buyPrice = scrapy.Field()  # 买价
    sellPrice = scrapy.Field()  # 卖价
    newestPrice = scrapy.Field()  # 最新价
    clearPrice = scrapy.Field()  # 结算价
    yestodayClearPrice = scrapy.Field()  # 昨结算
    buyQuantity = scrapy.Field()  # 买量
    sellQuantity = scrapy.Field()  # 卖量
    holdPosQuantity = scrapy.Field()  # 持仓量
    dealQuantity = scrapy.Field()  # 成交量
    tradeUnit = scrapy.Field()  # 商品交易所简称
    catogory = scrapy.Field()  # 品种名简称
    date = scrapy.Field()  # 日期
