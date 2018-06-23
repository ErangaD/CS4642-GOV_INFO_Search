from scrapy.spiders import CrawlSpider, Rule
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from w3lib.html import remove_tags, remove_tags_with_content
from scrapy.selector import Selector
import re

class MinistersSpider(CrawlSpider):
    name = 'crawler'
    allowed_domains = ["gic.gov.lk"]
    start_urls = ['http://www.gic.gov.lk/gic/index.php/en/component/org/']

    rules = (
        Rule(LinkExtractor(), callback = 'parse_item', follow=True, process_request='process_request'),
    )

    count = 1
    def parse_item(self, response):
        if ("en" in response.request.url):
            return
        sel = Selector(response)
        filename = "test/english/T" + str(self.count) + ".txt"
        tags_removed_text = remove_tags(remove_tags_with_content(sel.xpath('//body').extract()[0],which_ones=('script',)))
        tabs_removed_text = tags_removed_text.replace("\t", '').replace('\r', '')
        newLineRemovedText = re.sub(r'(\s*\n\s*)\1*', '\n', tabs_removed_text)
        with open(filename, "w") as out_file:
            for item in newLineRemovedText.split('\n'):
                out_file.write("%s\n" % item.strip())

        followed_urls = "followedTestURLs/englishUrls.txt"
        with open(followed_urls, "a") as out_file:
            out_file.write("%s\n" % response.request.url)
        self.count += 1
        print(self.count)

    def process_request(self, request):
        url = request.url
        if("component/org" in url) :
            return request
