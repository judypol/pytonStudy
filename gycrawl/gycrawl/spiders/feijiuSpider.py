from scrapy.spiders import Spider


class feijiuSpider(Spider):
    name = "feijiu"
    start_urls = [
        "http://baojia.feijiu.net/price-p-cid-bjcid2.-dqid-.html"
    ]
    allowed_domains = "baojia.feijiu.net"

    def start_requests(self):
        for p in self.start_urls:
            yield Request(url=p, )

    def parse(self, response):
