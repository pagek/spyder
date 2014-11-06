# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from scrapy.item import Item, Field

class MyItem(Item):
	url= Field()

class FenderSpider(CrawlSpider):
    name = "fender"
    allowed_domains = ["usedprice.com/"]
    start_urls = (
        'http://www.usedprice.com/items/guitars-musical-instruments/fender/?ob=model_asc#results',
    )
  
    rules = (
	Rule(SgmlLinkExtracto]/text()').extract()r(allow=()), callback='parse_url', follow=True),
    )

    def parse_url(self, response):

	item = MyItem()
	item['url'] = response.url
	item['data'] = response.xpath('//td')
	return item
	
        
