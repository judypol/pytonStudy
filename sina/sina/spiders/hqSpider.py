#!/usr/bin/python
# -*- coding: UTF-8 -*-

# !/usr/bin/python
# -*- coding: UTF-8 -*-

from scrapy.spiders import Spider
from scrapy.spiders import Request
import json
from sina.utils.urlUtils import UrlUtils
from sina.utils.dateTimeUtils import DateTimeUtils
from sina.items import SinaItem


class hqSpider(Spider):
    name = 'sinahq'
    urlTemplate = 'http://hq.sinajs.cn/?list={0}'
    start_urls = [

    ]
    products = [
        'V',
        'L',
        'PP',
        'MA',
        'SM',
        'AP'
    ]
    allowed_domains = ['hq.sinajs.cn']

    def start_requests(self):
        contractList = DateTimeUtils.getContractList()
        for pro in self.products:
            for contract in contractList:
                url = self.urlTemplate.format(pro + contract)
                yield Request(url=url, callback=self.parseItem)

    def parseItem(self, response):
        body = response.body_as_unicode().strip(';').strip('(').strip(')')
        bodyData = body[body.index('"') + 1:body.rindex('"')]
        if not bodyData or len(bodyData)<1:
            return

        datas = bodyData.split(',')

        hqItem = SinaItem()
        hqItem['name'] = datas[0]
        hqItem['time'] = datas[1]
        hqItem['openPrice'] = datas[2]
        hqItem['highestPrice'] = datas[3]
        hqItem['lowestPrice'] = datas[4]
        hqItem['yestodayClosePrice'] = datas[5]
        hqItem['buyPrice'] = datas[6]
        hqItem['sellPrice'] = datas[7]
        hqItem['newestPrice'] = datas[8]
        hqItem['clearPrice'] = datas[9]
        hqItem['yestodayClearPrice'] = datas[10]
        hqItem['buyQuantity'] = datas[11]
        hqItem['sellQuantity'] = datas[12]
        hqItem['holdPosQuantity'] = datas[13]
        hqItem['dealQuantity'] = datas[14]
        hqItem['tradeUnit'] = datas[15]
        hqItem['catogory'] = datas[16]
        hqItem['date'] = datas[17]
        # hqItem['dateAndTime']=datas[0]+datas[17]+"-"+datas[1]
        yield hqItem
