import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


# class AuthorSpider(scrapy.Spider):
class AuthorSpider(CrawlSpider):
    name = 'author'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = [
        'http://quotes.toscrape.com/'
    ]

    rules = [
        Rule(LinkExtractor(restrict_css=('.author + a')), callback="parse_author"),
        Rule(LinkExtractor(restrict_css=('li.next a')))
    ]

    # def parse(self, response):
    #     # follow links to author pages
    #     for href in response.css('.author + a::attr(href)'):
    #         yield response.follow(href, self.parse_author)
    #
    #     # follow pagination links
    #     for href in response.css('li.next a::attr(href)'):
    #         yield response.follow(href, self.parse)
    #
    # def parse_author(self, response):
    #     def extract_with_css(query):
    #         return response.css(query).get(default='').strip()
    #
    #     yield {
    #         'name': extract_with_css('h3.author-title::text'),
    #         'birthdate': extract_with_css('.author-born-date::text'),
    #         # 'bio': extract_with_css('.author-description::text'),
    #     }

    # ***************  Recommended approach  **************
    # def parse(self, response):
    #     yield from self.author_urls(response)
    #
    #     urls_s = response.css('li.next a')
    #     yield from [response.follow(url_s, callback=self.parse) for url_s in urls_s]
    #
    # def author_urls(self, response):
    #     # urls_s = response.css('div.quote a::attr(href)').getall()
    #     urls_s = response.css('.author + a::attr(href)').getall()
    #     return [response.follow(url_s, callback=self.parse_author) for url_s in urls_s]

    def parse_author(self, response):
        def extract_with_css(query):
            return response.css(query).get(default='').strip()

        yield {
            'name': extract_with_css('h3.author-title::text'),
            'birthdate': extract_with_css('.author-born-date::text'),
            # 'bio': extract_with_css('.author-description::text'),
        }
