from scrapy.spiders import Spider
from .. import items
from .. import settings
from scrapy import Request
from scrapy.selector import Selector


class feijiuSpider(Spider):
    handle_httpstatus_list = [400, 403, 404]
    max_page_count=200
    name = "feijiu"
    url_template='http://baojia.feijiu.net/price-p{page}-cid-bjcid2.-dqid-.html'
    start_urls = [
        url_template.format(page=x) for x in xrange(1, max_page_count)
    ]
    allowed_domains = ['feijiu.net']

    def start_requests(self):
        for p in self.start_urls:
            yield Request(url=p, headers=settings.DEFUALT_HEADER, callback=self.parse)

    def parse(self, response):
        bjurls = response.xpath('//div[@class="bjLists"]//@href').extract()
        if not bjurls:
            return
        for bjurl in bjurls:
            yield Request(url=bjurl, callback=self.parseItem)

    def parseItem(self, response):
        title = response.xpath('//div[@class="info_detail_article"]/h1/text()').extract_first()
        trs = response.xpath('//table[@class="MsoNormalTable"]//tr').extract()
        if not trs:
            return
        firstRow = True
        for tr in trs:
            if firstRow:
                firstRow = False
                continue
            tds = Selector(text=tr).xpath('//td//span/text()').extract()
            feiJiuItem = items.FeiJiuItem()
            feiJiuItem["source"] = title
            feiJiuItem["productName"] = tds[0]
            feiJiuItem["branch"] = tds[1]
            feiJiuItem["manufacturer"] = tds[2]
            feiJiuItem["price"] = tds[3]
            yield feiJiuItem
