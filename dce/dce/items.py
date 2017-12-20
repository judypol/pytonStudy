#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field


# 大商所夜行情
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


# 大商所日行情
class DceDayItem(scrapy.Item):
    commodity = Field()  # 商品名称
    deliveryMonth = Field()  # 交割月份
    openPrice = Field()  # 开仓价格
    maxPrice = Field()  # 最高价
    minPrice = Field()  # 最低价
    closePrice = Field()  # 收盘价
    preSettlementPrice = Field()  # 前结算价
    settlementPrice = Field()  # 结算价
    upsAndDowns = Field()  # 涨跌
    upsAndDownsOne = Field()  # 涨跌1
    volume = Field()  # 成交量
    position = Field()  # 持仓量
    changePosition = Field()  # 持仓量变化
    turnover = Field()  # 成交额
    date = Field()  # 爬取日期


class DceMemberItem(scrapy.Item):
    memberName = Field()
    volume = Field()  # 成交量
    change = Field()  # 增减
    date = Field()  # 爬取日期


class DceWeekItem(scrapy.Item):
    commodity = Field()  # 商品名称
    deliveryMonth = Field()  # 交割月份
    openPrice = Field()  # 周开盘价格
    maxPrice = Field()  # 最高价
    minPrice = Field()  # 最低价
    closePrice = Field()  # 收盘价
    settlementPrice = Field()  # 周结算价
    upsAndDowns = Field()  # 涨跌
    volume = Field()  # 成交量
    position = Field()  # 持仓量
    changePosition = Field()  # 持仓量变化
    turnover = Field()  # 成交额
    date = Field()  # 爬取日期


class DceMonthItem(scrapy.Item):
    commodity = Field()  # 商品名称
    deliveryMonth = Field()  # 交割月份
    openPrice = Field()  # 月开盘价格
    maxPrice = Field()  # 最高价
    minPrice = Field()  # 最低价
    closePrice = Field()  # 月收盘价
    settlementPrice = Field()  # 月结算价
    upsAndDowns = Field()  # 涨跌
    volume = Field()  # 成交量
    position = Field()  # 持仓量
    changePosition = Field()  # 持仓量变化
    turnover = Field()  # 成交额
    date = Field()  # 爬取日期
