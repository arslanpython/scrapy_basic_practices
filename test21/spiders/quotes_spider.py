import scrapy
from test21.items import quote


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url)
            # yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        qt = quote.Quote()
        for q in response.css('div.quote'):
            qt['text'] = q.css('span.text::text').get()
            qt['author'] = q.css('small.author::text').get()
            qt['tags'] = q.css('div.tags a.tag::text').getall()
            qt['headers'] = response.headers
            yield qt

            # yield {
            #     'page': page,
            #     'text': q.css('span.text::text').get(),
            #     'author': q.css('small.author::text').get(),
            #     'tags': q.css('div.tags a.tag::text').getall(),
            # }
