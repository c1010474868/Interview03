# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient
from .settings import MONGODB_HOST, MONGODB_PORT, DB, COLLECTION
import json


class QichezhijiaPipeline(object):

    # def open_spider(self, spider):
    #     self.file = open('meishi.json', 'a')
    #
    # def process_item(self, item, spider):
    #     result = json.dumps(dict(item), ensure_ascii=False, indent=2) + ',\n'
    #     self.file.write(result)
    #     return item
    #
    # def close_spider(self, spider):
    #     self.file.close()
    def open_spider(self, spider):
        con = MongoClient(host=MONGODB_HOST, port=MONGODB_PORT)
        print('*'*20)
        self.collection = con[DB][COLLECTION]

    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        return item