from scrapy.item import Field, Item


class XmlItem(Item):
    id = Field()
    name = Field()
    description = Field()
