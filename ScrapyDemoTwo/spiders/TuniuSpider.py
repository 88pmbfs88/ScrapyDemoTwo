# -*- coding: utf-8 -*-
import scrapy
from ScrapyDemoTwo import items

class TuniuSpider(scrapy.Spider):
    name = 'tuniuSpider'
    allowed_domains = ['tuniu.com']
    url = 'http://s.tuniu.com/search_complex/whole-yz-0-yunnan/'
    index = 1
    start_urls = [url+str(index)]

    def parse(self, response):

        info = response.xpath('//dl[@class="detail"]')
        for each in info:
            tcitem = items.TongchenItem()
            data_title = each.xpath('./dt/p[@class="title"]/span[@class="main-tit"]/span/text()').extract()[0].strip()
            data_introduction = each.xpath('./dt/p[@class="title"]/span[@class="main-tit"]/text()').extract()[1].strip()
            # data_label = each.xpath('./dt/p[@class="label"]').extract()
            tcitem['title'] = data_title
            tcitem['introduction'] = data_introduction
            # tcitem['label'] = data_label
            yield tcitem

        if self.index < 290:
             self.index += 1

        yield scrapy.Request(self.url+str(self.index), callback=self.parse)

