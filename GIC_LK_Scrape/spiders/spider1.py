import scrapy


from scrapy.loader import ItemLoader
import json



class QuotesSpider(scrapy.Spider):
    name = 'minister'
    allowed_domains = ["gic.gov.lk"]
    start_urls = ['http://www.gic.gov.lk/gic/index.php/en/component/org/?id=172&task=org']

    def parse(self, response):
        next_page = response.css('a::attr(href)').extract()
        print("URL: ---------------------------------------------------------------------" + response.request.url)
        for page in next_page:
            next_page = response.urljoin(page)
            yield scrapy.Request(next_page, callback=self.parse)
