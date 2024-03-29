import json
import scrapy


class InfiniteScroll(scrapy.Spider):
    name = 'infinite'
    api_url = 'http://quotes.toscrape.com/api/quotes?page={}'
    start_urls = [
        api_url.format(1)
    ]

    def parse(self, response):
        data = json.loads(response.text)
        for quote in data['quotes']:
            yield {
                'author': quote['author']['name'],
                'text': quote['text'],
                'tags': quote['tags']
            }
        if data['has_next']:
            next_page = data['page'] + 1
            yield scrapy.Request(self.api_url.format(next_page), callback=self.parse)
