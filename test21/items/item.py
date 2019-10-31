import scrapy
from scrapy import Item


class TestItem(Item):
    title = scrapy.Field(),
    description = scrapy.Field(),
    follow_link = scrapy.Field()
