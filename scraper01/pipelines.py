# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


import json

class Scraper01Pipeline(object):

    def __init__(self):
        self.fp = open("duanzi.json",'w',encoding='utf-8')

    def process_item(self, item, spider):
        # 注意，这里对象不能直接dump，应该转换为字典
        item_json = json.dumps(dict(item),ensure_ascii=False)
        self.fp.write(item_json+'\n')
        return item


    def open_spider(self,spider):
        print("爬虫开始了。。")
        # pass

    def close_spider(self,spider):
        self.fp.close()
        print("爬虫结束了")
    #    pass 
