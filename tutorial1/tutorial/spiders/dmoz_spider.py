from scrapy.spiders import Spider
from scrapy.selector import Selector
from .. import items


class DmozSpider(Spider):
    handle_httpstatus_list = [400, 403]
    name = "dmoz"
    allowed_domains = ['dmoz.org']
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]

    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath('//p')
        # dmozItems = []
        for site in sites:
            item = items.DmozItem()
            item['title'] = site.xpath('a/text()').extract()
            item['link'] = site.xpath('a/@href').extract()
            item['desc'] = site.xpath('text()').extract()
            # dmozItems.append(item)
        yield item
