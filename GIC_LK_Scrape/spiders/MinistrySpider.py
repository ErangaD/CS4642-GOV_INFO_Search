from scrapy.spiders import CrawlSpider, Rule
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from w3lib.html import remove_tags, remove_tags_with_content
from scrapy.selector import Selector
import re

class MinistersSpider(CrawlSpider):
    name = 'ministrySpider'
    allowed_domains = ["parliament.lk"]
    start_urls = ['http://www.parliament.lk/']

    rules = (
        Rule(LinkExtractor(), callback='parse_item', follow=True),
    )

    count = 0
    def parse_item(self, response):

        print("URL: ---------------------------------------------------------------------" + response.request.url)

        sel = Selector(response)
        filename = "data/T"+str(self.count)+".txt"
        self.count+=1
        tags_removed_text = remove_tags(remove_tags_with_content(sel.xpath('//body').extract()[0],which_ones=('script',)))
        tabs_removed_text = tags_removed_text.replace("\t", '').replace('\r', '')
        newLineRemovedText = re.sub(r'(\n)\1*', '\n', tabs_removed_text)
        with open(filename, "w") as out_file:
            for item in newLineRemovedText.split('\n'):
                out_file.write("%s\n" % item.strip())

        # for page in next_pages:
        #     next_page = response.urljoin(page)
        #     yield scrapy.Request(next_page, callback=self.parse_ministry)

