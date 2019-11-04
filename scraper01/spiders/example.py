# -*- coding: utf-8 -*-
import scrapy
# from scrapy.http.response.html import HtmlResponse

# from scrapy.selector.unified import SelectorList

from scraper01.items import Scraper01Item

class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['www.lovehhy.net']
    start_urls = ['http://www.lovehhy.net/Joke/Detail/QSBK/1/']

    def parse(self, response):
        # 页面中解析数据
        # div = response.xpath("//div[@id='footzoon']")
        # https: // blog.csdn.net/Dome_/article/details/80638245
        # 这里的xpath语法需要说一下
        divs = response.xpath("//div[@id='endtext']")

        for duanzidiv  in divs:
            content = duanzidiv.xpath("./text()").getall()
            content = "".join(content).strip()
            # 导入content
            item = Scraper01Item(content= content)

            yield item
            # yield {'content':content}


