import logging
import scrapy

logger = logging.getLogger('mycustomlogger')

class BooksSpider(scrapy.Spider):
    name = 'myspider'
    #logger.info(url)
    logger.info('Hello World')
    def start_requests(self):
        yield scrapy.Request(url='https://www.w3schools.com/', callback=self.parse)

    def parse(self, response):
        page = response.url
        
    
