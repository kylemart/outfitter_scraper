# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class OutfittrScraperItem(scrapy.Item):
    clothing = scrapy.Field()
    image_items = scrapy.Field()
    images = scrapy.Field()
