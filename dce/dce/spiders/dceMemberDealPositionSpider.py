#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Time : 2017/1/1 17:51
# @Author : lzh
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy import Request

from utils.dateUtils import DateUtils
from .. import items


class dceMemberDealPositionSpider(Spider):
    name = "dceMember"  # name是必须的
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
    urlTemplate = 'http://www.dce.com.cn/publicweb/quotesdata/memberDealPosiQuotes.html?memberDealPosiQuotes.variety=a&memberDealPosiQuotes.trade_type=0&year=2017&month=12&day=17&contract.contract_id=all&contract.variety_id=a'
    start_urls = [
        urlTemplate
    ]

    def start_requests(self):
        for requestUrl in self.start_urls:
            yield Request(url=requestUrl, headers=self.defaultHeader, callback=self.parse)

    def parse(self, response):
        tableAreas = response.xpath('//div[@class="dataArea"]//table[2]//tr').extract()
        firstRow = True  # 是否是第一行
        dceMemberItems=[]
        #获取所有的会员信息，一行有3组信息
        for tr in tableAreas:
            if firstRow:
                firstRow = False
                continue

            tds = Selector(text=tr).xpath('//td/text()').extract()

            dceMemberItem1 = items.DceMemberItem()
            dceMemberItem1["memberName"] = tds[1].replace('\t', '').replace('\n', '').strip()
            dceMemberItem1["volume"] = tds[2].replace('\t', '').replace('\n', '').strip()
            dceMemberItem1["change"] = tds[3].strip().replace('\t', '').replace('\n', '').strip()
            dceMemberItem1["date"]=dateUtils.getDateString()
            dceMemberItems.append(dceMemberItem1)

            dceMemberItem1 = items.DceMemberItem()
            dceMemberItem1["memberName"] = tds[5].replace('\t', '').replace('\n', '').strip()
            dceMemberItem1["volume"] = tds[6].replace('\t', '').replace('\n', '').strip()
            dceMemberItem1["change"] = tds[7].strip().replace('\t', '').replace('\n', '').strip()
            dceMemberItem1["date"] = dateUtils.getDateString()
            dceMemberItems.append(dceMemberItem1)

            dceMemberItem1 = items.DceMemberItem()
            dceMemberItem1["memberName"] = tds[9].replace('\t', '').replace('\n', '').strip()
            dceMemberItem1["volume"] = tds[10].replace('\t', '').replace('\n', '').strip()
            dceMemberItem1["change"] = tds[11].strip().replace('\t', '').replace('\n', '').strip()
            dceMemberItem1["date"] = DateUtils.getDateString()
            dceMemberItems.append(dceMemberItem1)

        for memberItem in dceMemberItems:
            yield memberItem
