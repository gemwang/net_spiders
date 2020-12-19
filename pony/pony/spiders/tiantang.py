import scrapy


class TiantangSpider(scrapy.Spider):
    name = 'tiantang'
    allowed_domains = ['dy2018.com']
    start_urls = ['http://dy2018.com/']

    def parse(self, response):
        pass
