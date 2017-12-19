# -*- coding: utf-8 -*-
# @Time : 2017/1/1 17:51
# @Author : lzh
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy import Request
from .. import items


class dceDaySpider(Spider):
    name = "dceDay"  # name是必须的
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
    urlTemplate = 'http://www.dce.com.cn/publicweb/quotesdata/dayQuotesCh.html?dayQuotes.variety=all&dayQuotes.trade_type=0&year=2017&month=11&day=18'
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
            dceDayItem = items.DceDayItem()
            dceDayItem["commodity"] = tds[0].replace('\t', '').replace('\n', '').strip()
            dceDayItem["deliveryMonth"] = tds[1].replace('\t', '').replace('\n', '').strip()
            dceDayItem["openPrice"] = tds[2].strip().replace('\t', '').replace('\n', '').strip()
            dceDayItem["maxPrice"] = tds[3].strip().replace('\t', '').replace('\n', '').strip()
            dceDayItem["minPrice"] = tds[4].strip().replace('\t', '').replace('\n', '').strip()
            dceDayItem["closePrice"] = tds[5].strip().replace('\t', '').replace('\n', '').strip()
            dceDayItem["preSettlementPrice"] = tds[6].strip().replace('\t', '').replace('\n', '').strip()
            dceDayItem["settlementPrice"] = tds[7].strip().replace('\t', '').replace('\n', '').strip()
            dceDayItem["upsAndDowns"] = tds[8].strip().replace('\t', '').replace('\n', '').strip()
            dceDayItem["upsAndDownsOne"] = tds[7].strip().replace('\t', '').replace('\n', '').strip()
            dceDayItem["volume"] = tds[9].strip().replace('\t', '').replace('\n', '').strip()
            dceDayItem["position"] = tds[10].strip().replace('\t', '').replace('\n', '').strip()
            dceDayItem["changePosition"] = tds[11].strip().replace('\t', '').replace('\n', '').strip()
            dceDayItem["turnover"] = tds[12].strip().replace('\t', '').replace('\n', '').strip()
            yield dceDayItem
