import scrapy
from scrapy.loader import ItemLoader
import json


#
# class QuotesSpider(scrapy.Spider):
#     name = 'minister'
#     allowed_domains = ["gic.gov.lk"]
#     start_urls = ['http://www.cabinetoffice.gov.lk/cab/index.php?option=com_content&view=article&id=15&Itemid=49&lang=en&dDate=2017-07-18']
#
#     def parse(self, response):
#         next_page = response.css('a::attr(href)').extract()
#         # print(next_page)
#         for page in next_page:
#             pageToGo = response.urljoin(page)
#             print("URL: ---------------------------------------------------------------------")
#             print(pageToGo)
#             yield scrapy.Request(pageToGo, callback=self.parse)

class QuotesSpider(scrapy.Spider):
    name = 'minister'

    allowed_domains = ["cabinetoffice.gov.lk"]
    start_urls = ['http://www.cabinetoffice.gov.lk/cab/index.php?option=com_content&view=article&id=15&Itemid=49&lang=en&dDate=2017-07-18']

    def parse(self, response):
        page = response.url.split("&lang=")

        print("************************************************************************")
        print(page)