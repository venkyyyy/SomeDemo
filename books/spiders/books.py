import scrapy
class BooksSpider(scrapy.Spider):
    name = 'myspider'
    self.log('Hello World')
    def start_requests(self):
        yield scrapy.Request(url='https://www.w3schools.com/', callback=self.parse)

    def parse(self, response):
        page = response.headers
        self.log(page)        
    
