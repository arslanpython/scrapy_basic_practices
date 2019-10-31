import scrapy
from scrapy.loader import ItemLoader
from test21.items import quote


class QuotesSpider(scrapy.Spider):
    name = "item"
    start_urls = ['http://quotes.toscrape.com/tag/change/page/1/']

    def parse(self, response):
        # yield {
        #     'text': response.css('span.text::text').get(),
        #     'author': response.css('small.author::text').get(),
        #     'tags': response.css('div.tags a.tag::text').getall(),
        # }

        #  OR Use Loader
        # loader = ItemLoader(item=quote.Quote(), response=response)
        loader = ItemLoader(quote.Quote(), response)
        loader.add_css('text', 'span.text::text')
        loader.add_css('author', 'small.author::text')
        loader.add_css('tags', 'div.tags a.tag::text')

        return loader.load_item()





