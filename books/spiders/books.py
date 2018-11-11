# -*- coding: utf-8 -*-
import scrapy
from ..items import BooksItem


class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["www.google.co.in"]
    start_urls = [
        'https://www.google.co.in/search?q=Prime+Air+in+US-WA-Seattle&ibp=htl;jobs',
    ]



    def parse(self, response):
          item= BooksItem()
          item['body']=response.body
          yield item
