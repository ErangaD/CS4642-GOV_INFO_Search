import scrapy
from bs4 import BeautifulSoup


class QuotesSpider(scrapy.Spider):
    name = "general"
    count = 0

    allowed_domains = ["slelections.gov.lk"]
    start_urls = ['http://www.gic.gov.lk/gic/index.php/en/component/org/?id=4&task=cat']

    def parse(self, response):
        body = response.body
        soup = BeautifulSoup(body)
        self.count = self.count + 1

        print("********************* %d ************************" % (self.count))

        # Saving the page
        page = response.url.split("/")[-2]
        filename = 'data/data-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(body)
        self.log('Saved file %s' % filename)

        # Extracting links
        # links = soup.find_all('a')
        # for link in links:
        #     next_route = link.get('href')
        #     yield response.follow(next_route, callback=self.parse)
