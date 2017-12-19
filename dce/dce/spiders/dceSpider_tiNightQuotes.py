# -*- coding: utf-8 -*-
# @Time : 2017/1/1 17:51
# @Author : lzh
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy import Request
from .. import items


class dceSpider(Spider):
    name = "dce_night"  # name是必须的
    defaultHeader = {  # 请求头
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Cookie': 'ASP.NET_SessionId=j5zgme3wavrchcsqez1ljtau; _ga=GA1.2.868326836.1513564049; _gid=GA1.2.1542499785.1513564049',
        'Host': 'www.dce.com.cn',
        'Pragma': 'no-cache',
        'Upgrade-Insecure-Requests': 1,
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
    }
    allowed_domains = ['dce.com.cn']
    urlTemplate = 'http://www.dce.com.cn/publicweb/quotesdata/tiNightQuotes.html?tiNightQuotes.variety=all&tiNightQuotes.trade_type=0&year=2017&month=10&day=13'
    start_urls = [
        urlTemplate
    ]

    def start_requests(self):
        for requestUrl in self.start_urls:
            yield Request(url=requestUrl, headers=self.defaultHeader, callback=self.parse)

    def parse(self, response):
        tableAreas = response.xpath('//div[@class="dataArea"]//table//tr').extract()
        firstRow = True  # 是否是第一行
        for tr in tableAreas:
            if firstRow:
                firstRow = False
                continue

            tds = Selector(text=tr).xpath('//td/text()').extract()
            dceNightItem = items.DceNightItem()
            dceNightItem["varieties"] = tds[0].replace('\t', '').replace('\n', '').strip()
            dceNightItem["deliveryMonth"] = tds[1].replace('\t', '').replace('\n', '').strip()
            dceNightItem["openPrice"] = tds[2].strip().replace('\t', '').replace('\n', '').strip()
            dceNightItem["maxPrice"] = tds[3].strip().replace('\t', '').replace('\n', '').strip()
            dceNightItem["minPrice"] = tds[4].strip().replace('\t', '').replace('\n', '').strip()
            dceNightItem["latestPrice"] = tds[5].strip().replace('\t', '').replace('\n', '').strip()
            dceNightItem["upsAndDowns"] = tds[6].strip().replace('\t', '').replace('\n', '').strip()
            dceNightItem["price"] = tds[7].strip().replace('\t', '').replace('\n', '').strip()
            dceNightItem["preSettlementPrice"] = tds[8].strip().replace('\t', '').replace('\n', '').strip()
            dceNightItem["volume"] = tds[9].strip().replace('\t', '').replace('\n', '').strip()
            dceNightItem["position"] = tds[10].strip().replace('\t', '').replace('\n', '').strip()
            dceNightItem["changePosition"] = tds[11].strip().replace('\t', '').replace('\n', '').strip()
            dceNightItem["turnover"] = tds[12].strip().replace('\t', '').replace('\n', '').strip()
            yield dceNightItem
