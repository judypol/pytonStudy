#!/usr/bin/python
# -*- coding: UTF-8 -*-

#!/usr/bin/python
# -*- coding: UTF-8 -*-

from scrapy.spiders import Spider
from scrapy.spiders import Request
import json
from sina.utils.urlUtils import UrlUtils
from sina.utils.dateTimeUtils import DateTimeUtils

class hqSpider(Spider):
    name = 'sinahq'
    urlTemplate='http://hq.sinajs.cn/list={0}'
    start_urls = [

    ]
    products=[
        'V',
        'L',
        'PP',
        'MA',
        'SM'
    ]
    allowed_domains = ['hq.sinajs.cn']

    def start_requests(self):
        contractList = DateTimeUtils.getContractList()
        for pro in self.products:
            for contract in contractList:
                url = self.urlTemplate.format(pro+contract)
                yield Request(url=url, callback=self.parseItem)

    def parseItem(self, response):
        body=response.body_as_unicode().strip(';').strip('(').strip(')')
        bodyData=body[body.index('"')+1:body.rindex('"')]
        jsonData = json.loads(response.body_as_unicode().strip(';').strip('(').strip(')'))
        datas = jsonData['Data'][0]
        contractCode = self.getContractName(response)


    def getContractName(self, response):
        code = UrlUtils.getQueryValue(response.url, 'code')[-4:]
        return self.name + code
