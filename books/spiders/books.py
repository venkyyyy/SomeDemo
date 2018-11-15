import scrapy
from scrapy_splash import SplashRequest

class MySpider(scrapy.Spider):
    name="quotes"
    start_urls = ["https://www.google.com/search?q=jobs+near+me&ibp=htl;jobs&sa=X&ved=2ahUKEwi56qSsu9beAhUEo48KHSKfDmYQiYsCKAB6BAgGEAM#fpstate=tldetail&htidocid=4UtjOLd3b4R-NFTwAAAAAA%3D%3D&htivrt=jobs"]

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse,
                endpoint='render.html',
                args={'wait': 0.5},
            )

    def parse(self, response):
        yield{
       'body':response.body
       } 
