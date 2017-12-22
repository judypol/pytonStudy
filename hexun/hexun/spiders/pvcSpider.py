#!/usr/bin/python
# -*- coding: UTF-8 -*-

from scrapy.spiders import Spider
from scrapy.spiders import Request
import json
from items import HexunItem
from utils.urlUtils import UrlUtils
from utils.dateTimeUtils import DateTimeUtils

class PVCSpider(Spider):
    name = 'pvc'
    urlTemplate='http://webftcn.hermes.hexun.com/shf/minute?code=DCEv{0}&start={1}&number=225&t=1513834850784'
    start_urls = [

    ]
    allowed_domains = ['*.hexun.com']

    def start_requests(self):
        contractList = DateTimeUtils.getContractList()
        for contract in contractList:
            url = self.urlTemplate.format(contract, DateTimeUtils.getStartTime())
            yield Request(url=url, callback=self.parseItem)

    def parseItem(self, response):
        jsonData = json.loads(response.body_as_unicode().strip(';').strip('(').strip(')'))
        datas = jsonData['Data'][0]
        contractCode = self.getContractName(response)
        for dataItem in datas:
            lldpeItem = HexunItem()
            lldpeItem['product'] = contractCode
            lldpeItem['dateTime'] = dataItem[0]
            lldpeItem['price'] = dataItem[1]
            lldpeItem['amount'] = dataItem[2]
            lldpeItem['volumn'] = dataItem[3]
            lldpeItem['avePrice'] = dataItem[4]
            lldpeItem['openInterest'] = dataItem[5]
            yield lldpeItem

    def getContractName(self, response):
        code = UrlUtils.getQueryValue(response.url, 'code')[-4:]
        return self.name + code
