# -*- coding: utf-8 -*-
import scrapy


class YirenSpider(scrapy.Spider):
    name = 'yiren'
    allowed_domains = ['yiren.com']
    start_urls = ['https://yiren.com/']

    def parse(self, response):
        print(response.text)
