import scrapy


class ArgumentSpider(scrapy.Spider):
    name = 'argument'

    def start_requests(self):
        url = 'http://quotes.toscrape.com/'
        tag = getattr(self, 'tag', None)
        if tag is not None:
            url = url + 'tag/' + tag

        yield scrapy.Request(url, self.parse)

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'author': quote.css('.author::text').get(),
                'quote': quote.css('.text::text').get(),
            }

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)


#  Command line pass argument likescrapy sh
#  scrapy crawl quotes -a tag=humor
