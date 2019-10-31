import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from test21.items.item import TestItem
from test21.items import quote


class CrawlSpiderExample(CrawlSpider):
    name = 'links'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    # rules = (
    #     # Rule(LinkExtractor(allow=r'page/[\d]+', canonicalize=True), follow=True, callback='parse_item'),
    #     # Rule(LinkExtractor(), follow=True, callback='parse_item'),
    #     Rule(LinkExtractor(restrict_css=('li.next a')), follow=True, callback='parse_item'),
    # )

    rules = [
        Rule(LinkExtractor(restrict_css=('li.next a')), follow=True, callback='parse_item')
    ]

    def parse_item(self, response):
        for q in response.css('div.quote'):
            qt = quote.Quote()
            qt['text'] = q.css('span.text::text').get()
            qt['author'] = q.css('small.author::text').get()
            qt['tags'] = q.css('div.tags a.tag::text').getall()
            yield qt
