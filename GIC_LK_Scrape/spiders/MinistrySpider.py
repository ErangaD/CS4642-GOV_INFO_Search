from scrapy.spiders import CrawlSpider, Rule
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from w3lib.html import remove_tags, remove_tags_with_content
from scrapy.selector import Selector
import re

class MinistersSpider(CrawlSpider):
    name = 'crawler'
    allowed_domains = ["gic.gov.lk"]
    start_urls = ['http://www.gic.gov.lk/gic/index.php/en/component/org/?id=172&task=org']

    rules = (
        Rule(LinkExtractor(), callback='parse_item', follow=True),
    )

    count = 0
    def parse_item(self, response):

        print("URL: ---------------------------------------------------------------------" + str(self.count))

        sel = Selector(response)
        self.count+=1

        filename = "data/T" + str(self.count) + ".txt"
        tags_removed_text = remove_tags(remove_tags_with_content(sel.xpath('//body').extract()[0],which_ones=('script',)))
        tabs_removed_text = tags_removed_text.replace("\t", '').replace('\r', '')
        newLineRemovedText = re.sub(r'(\s*\n\s*)\1*', '\n', tabs_removed_text)
        with open(filename, "w") as out_file:
            for item in newLineRemovedText.split('\n'):
                out_file.write("%s\n" % item.strip())


