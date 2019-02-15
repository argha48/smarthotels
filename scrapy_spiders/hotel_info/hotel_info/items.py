# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HotelInfoItem(scrapy.Item):
    # define the fields for your item here like:
    HotelID = scrapy.Field()
    HotelName = scrapy.Field()
    # ReviewUrl = scrapy.Field()
    HotelAddress = scrapy.Field()
    HotelCoordinate = scrapy.Field()
    Facilities = scrapy.Field()
    MainFacilities = scrapy.Field()
    ImageUrls = scrapy.Field()
