import scrapy


class LoginSpider(scrapy.Spider):
    name = 'login'
    login_url = 'http://quotes.toscrape.com/login'

    start_urls = [
        login_url,
    ]

    def parse(self, response):
        # extract the csrf_token for login
        token = response.css('input[name=csrf_token]::attr(value)').get()
        # create dictionary for form arguments
        data = {
            'csrf_token': token,
            'username': 'abc',
            'password': 'abc',
        }
        # submit post request
        return scrapy.FormRequest(self.login_url, formdata=data, callback=self.parse_quotes)
        # return scrapy.FormRequest(response.url, formdata=data, callback=self.parse_quotes)
        # return scrapy.FormRequest.from_response(response, formdata=data, callback=self.parse_quotes)

    def parse_quotes(self, response):
        for q in response.css('div.quote'):
            yield {
                'name': q.css('.author::text').get(),
                # 'author_url': q.css('div.quote span a:last-child[href*="goodreads.com"]::attr(href)').get(),
                'author_url': q.css('.author ~ a[href*="goodreads.com"]::attr(href)').get(),
            }
