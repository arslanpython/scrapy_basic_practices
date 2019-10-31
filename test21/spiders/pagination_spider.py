import scrapy


class QuotesSpider(scrapy.Spider):
    name = "pagination"
    start_urls = [
        'http://quotes.toscrape.com/'
    ]

    def parse(self, response):
        # page = response.url.split("/")[-2]
        for q in response.css('div.quote'):
            yield {
                'page': '',
                'text': q.css('span.text::text').get(),
                'author': q.css('small.author::text').get(),
                'tags': q.css('div.tags a.tag::text').getall(),
            }

            # next = response.css('li.next a::attr(href)').get()
            # print('Join -->', response.urljoin(next))
            # print('Follow -->', response.follow(next))

            # next_follow = response.css('li.next a').get()
            # print('Follow -->', response.follow(next_follow, self.parse))  #  Invalid  We will get error it,
            #  HTTP status code is not handled or not allowed

            # follow pagination links
            next_page = response.css('li.next a::attr(href)').get()
            if next_page is not None:
                yield response.follow(next_page, callback=self.parse)
            #  OR
            # for href in response.css('li.next a'):  #  'li.next a' it only work in for loop
            #     yield response.follow(href, callback=self.parse)
