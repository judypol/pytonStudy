# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field


class DceNightItem(scrapy.Item):
    varieties = Field()  # 品种
    deliveryMonth = Field()  # 交割月份
    openPrice = Field()  # 开仓价格
    maxPrice = Field()  # 最高价
    minPrice = Field()  # 最低价
    latestPrice = Field()  # 最新价
    upsAndDowns = Field()  # 涨跌
    price = Field()  # 买价/卖价
    preSettlementPrice = Field()  # 前结算价
    volume = Field()  # 成交量
    position = Field()  # 持仓量
    changePosition = Field()  # 持仓量变化
    turnover = Field()  # 成交额
