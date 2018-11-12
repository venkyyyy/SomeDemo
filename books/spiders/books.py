import logging
import scrapy
from ..items import BooksItem


logger = logging.getLogger('mycustomlogger')

class BooksSpider(scrapy.Spider):

    name = 'myspider'
    start_urls = ['https://scrapinghub.com']

    def parse(self, response):
        logger.info('Parse function called on %s', response.url)
        item= BooksItem()
        item['body']=response.body
        yield item
          
