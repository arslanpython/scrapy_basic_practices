from scrapy.spiders import XMLFeedSpider
from test21.items.xml_item import XmlItem


class MySpider(XMLFeedSpider):
    name = 'xmlfeed'
    allowed_domains = ['zillow.com']
    start_urls = ['https://www.zillow.com/sitemap/catalog/cdp/index.xml']
    iterator = 'iternodes'  # This is actually unnecessary, since it's the default value
    itertag = 'item'

    def parse_node(self, response, node):
        self.logger.info('Hi, this is a <%s> node!: %s', self.itertag, ''.join(node.extract()))
        print(response.text)

        item = XmlItem()
        item['id'] = node.xpath('sitemap').extract()
        item['name'] = node.xpath('loc').extract()
        item['description'] = node.xpath('//sitemap/loc/text()').extract()
        return item
