import scrapy


class Quote(scrapy.Item):
    text = scrapy.Field()
    author = scrapy.Field()
    tags = scrapy.Field()
    headers = scrapy.Field()
    test = scrapy.Field()
    t = scrapy.Field()
