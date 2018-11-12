import logging
import scrapy
from ..items import BooksItem


logger = logging.getLogger('mycustomlogger')

class BooksSpider(scrapy.Spider):

    name = 'myspider'
    #start_urls = ['https://scrapinghub.com']

    #def parse(self, response):
    url_get = self.request.GET
    logger.info(url_get)
    logger.info('Hello World')
