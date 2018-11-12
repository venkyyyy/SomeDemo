import logging
import scrapy
from ..items import BooksItem


logger = logging.getLogger('mycustomlogger')

class BooksSpider(scrapy.Spider):

    name = 'myspider'
    #start_urls = ['https://scrapinghub.com']

    #def parse(self, response):
    logger.info('Hello World')
