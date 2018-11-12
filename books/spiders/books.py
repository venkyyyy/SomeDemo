# -*- coding: utf-8 -*-
import scrapy
from ..items import BooksItem
import logging


class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["www.google.co.in"]
    start_urls = [
        'https://www.google.co.in/search?q=Prime+Air+in+US-WA-Seattle&ibp=htl;jobs',
    ]
     for url in start_urls:
            # We make a request to each url and call the parse function on the http response.
			yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
          item= BooksItem()
          item['body']=response.body
          #self.log(" Entered !! ")
          logging.warning("This is a warning")
          yield item
