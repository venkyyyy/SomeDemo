import scrapy


class QuotesSpider(scrapy.Spider):
   name = "quotes"
   start_urls = [
      'https://www.google.com/search?q=jobs+near+me&ibp=htl;jobs&sa=X&ved=2ahUKEwi56qSsu9beAhUEo48KHSKfDmYQiYsCKAB6BAgGEAM#fpstate=tldetail&htidocid=4UtjOLd3b4R-NFTwAAAAAA%3D%3D&htivrt=jobs'
   ]

   def parse(self, response):
       #for quote in response.css('div.gRTukd T2uyV'):
       #with open('D://outputs//hie.txt','w',encoding='utf-8') as U:
       # U.write(str(response.body))
       
       yield{
       'body':response.body
       } 
