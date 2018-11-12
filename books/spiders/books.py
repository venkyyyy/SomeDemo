import logging
import scrapy

logger = logging.getLogger('mycustomlogger')

class BooksSpider(scrapy.Spider):
    name = 'myspider'
    logger.info(url)
    logger.info('Hello World')
    
