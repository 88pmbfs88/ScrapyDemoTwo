# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


# class ScrapydemotwoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass

class TongchenItem(scrapy.Item):
    # 标题
    title = scrapy.Field()
    # 简介
    introduction = scrapy.Field()
    # 详细描述
    detail = scrapy.Field()
    # 营业时间
    business_time = scrapy.Field()
    # 标签
    label = scrapy.Field()
    # 酒店
    hotel = scrapy.Field()
    # 价格
    price = scrapy.Field()
    # 满意度
    satisfaction = scrapy.Field()
    # 评价
    comment = scrapy.Field() 