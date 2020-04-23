# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonProduct(scrapy.Item):
    title = scrapy.Field()
    rating = scrapy.Field()
    price = scrapy.Field()
    colour = scrapy.Field()
    description = scrapy.Field()
    reviews = scrapy.Field()
    brand = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()
    website = scrapy.Field()
    url = scrapy.Field()
