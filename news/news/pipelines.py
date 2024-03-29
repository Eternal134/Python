# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class NewsPipeline(object):
    def __init__(self):
        self.f = open("data.json" , "w", encoding = 'utf-8')

    def process_item(self, item, spider):
        data = json.dump(dict(item) , self.f , ensure_ascii = False)
        self.f.write('\n')
#        self.f.write(data)
        return item

    def close_spider(self , spider):
        self.f.close()
