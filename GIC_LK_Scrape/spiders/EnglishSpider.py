from scrapy.spiders import CrawlSpider, Rule
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from w3lib.html import remove_tags, remove_tags_with_content
from scrapy.selector import Selector
from GIC_LK_Scrape.items import OrgItem
import csv
import re

class EnglishSpider(CrawlSpider):
    name = 'englishCrawler'
    allowed_domains = ["gic.gov.lk"]
    start_urls = ['http://www.gic.gov.lk/gic/index.php/en/component/org/']

    rules = (
        Rule(LinkExtractor(), callback = 'parse_item', follow=True, process_request='process_request'),
    )

    count = 1
    file_name = open('Output_file.csv', 'w')  # Output_file.csv is name of output file

    fieldnames = ['text', 'link']  # adding header to file
    writer = csv.DictWriter(file_name, fieldnames=fieldnames)
    writer.writeheader()
    def parse_item(self, response):
        sel = Selector(response)
        filename = "test/english/T" + str(self.count) + ".txt"
        tags_removed_text = remove_tags(remove_tags_with_content(sel.xpath('//*[@id="ja-content"]').extract()[0],which_ones=('script',)))
        tabs_removed_text = tags_removed_text.replace("\t", '').replace('\r', '')
        newLineRemovedText = re.sub(r'(\s*\n\s*)\1*', '\n', tabs_removed_text)
        # with open(filename, "w") as out_file:
        #     for item in newLineRemovedText.split('\n'):
        #         out_file.write("%s\n" % item.strip())
        #
        # followed_urls = "followedTestURLs/englishUrls.txt"
        # with open(followed_urls, "a") as out_file:
        #     out_file.write("%s\n" % response.request.url)
        # docum = OrgItem()
        # docum['text'] = newLineRemovedText
        # docum['link'] = response.request.url

        self.writer.writerow(
                {'text': newLineRemovedText, 'link': response.request.url})  # writing data into file.
        self.count += 1
        print(self.count)

    def process_request(self, request):
        url = request.url
        if("component/org" in url):
            if ("/en/" in url):
                return request
