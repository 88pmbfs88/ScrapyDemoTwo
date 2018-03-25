# -*- coding: utf-8 -*-
import scrapy


class GirlspicspiderSpider(scrapy.Spider):
    name = 'girlsPICspider'
    allowed_domains = ['www.27270.com']
    start_urls = ['http://www.27270.com/ent/meinvtupian/']

    def parse(self, response):
        with open('index.html','w') as f :
            f.write(response.body)
