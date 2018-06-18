import scrapy
from scrapy.loader import ItemLoader
import json



class QuotesSpider(scrapy.Spider):
    name = 'minister'
    allowed_domains = ["gic.gov.lk"]
    start_urls = ['http://www.gic.gov.lk/gic/index.php/en/component/org/?id=172&task=org']

    def parse(self, response):
        next_page = response.css('a::attr(href)').extract()
        # print(next_page)
        for page in next_page:
            pageToGo = response.urljoin(page)
            print("URL: ---------------------------------------------------------------------")
            print(pageToGo)
            yield scrapy.Request(pageToGo, callback=self.parse)
