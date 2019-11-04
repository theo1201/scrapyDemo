# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Scraper01Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 这里可以固定传递的参数
    content = scrapy.Field()

