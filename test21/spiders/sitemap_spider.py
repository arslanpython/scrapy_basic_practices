from scrapy.spiders import SitemapSpider


class SiteMapSpider(SitemapSpider):
    name = 'sitemap'

    sitemap_urls = [
        'https://www.zillow.com/sitemap/catalog/cdp/index.xml',
    ]

    def parse(self, response):
        # print(response.text)
        pass
