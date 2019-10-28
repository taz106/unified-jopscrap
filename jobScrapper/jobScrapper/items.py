# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JobscrapperItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    description = scrapy.Field()
    company_name = scrapy.Field()
    location = scrapy.Field()
    ad_url = scrapy.Field()

class QuoteItem(scrapy.Item):
    content = scrapy.Field()
    author = scrapy.Field()
