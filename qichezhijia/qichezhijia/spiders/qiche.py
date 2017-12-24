# -*- coding: utf-8 -*-
import scrapy
from copy import deepcopy


class QicheSpider(scrapy.Spider):
    name = 'qiche'
    allowed_domains = ['www.autohome.com.cn']
    start_urls = ['https://www.autohome.com.cn']

    def parse(self, response):
        url_list = response.xpath("//div[@class='navcar']/ul/li/a/@href").extract()
        print(url_list)
        for url in url_list:
            url = 'https:' + url
            yield scrapy.Request(
                url,
                callback=self.parse_detail
            )

    def parse_detail(self, response):
        item = dict()
        item["b_cate"] = response.xpath("//span[@class='filter-text']/text()").extract_first()
        dl_list = response.xpath("//div[@class='uibox']/div[2]/dl")
        for dl in dl_list:
            item["m_cate_name"] = dl.xpath("./dd/div/text()").extract_first()
            item["s_cate_name"] = dl.xpath("./dd//h4/a/text()").extract()
            item["s_cate_href"] = dl.xpath("./dd//h4/a/@href").extract()
            for url in item["s_cate_href"]:
                url = 'https:' + url
                yield scrapy.Request(
                    url,
                    meta={"item": deepcopy(item)},
                    callback=self.parse_detail_d
                )

    def parse_detail_list(self, response):
        item = response.meta["item"]
        item["s_cate_name_score"] = response.xpath("//div[@class='koubei-score']/text()")

