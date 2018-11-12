import logging
import scrapy
from ..items import BooksItem
import os

logger = logging.getLogger('mycustomlogger')

class BooksSpider(scrapy.Spider):

    name = 'myspider'
    #start_urls = ['https://scrapinghub.com']
    url = os.environ['HTTP_HOST']

    #def parse(self, response):
    #url_get = self.request.GET
    logger.info(url)
    logger.info('Hello World')
