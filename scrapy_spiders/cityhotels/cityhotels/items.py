# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class CityhotelsItem(scrapy.Item):
    # define the fields for your item here like:
    # HotelID = scrapy.Field()
    HotelName = scrapy.Field()
    HotelUrl = scrapy.Field()
    HotelReviewUrl = scrapy.Field()
    # ReviewScore = scrapy.Field()
    # NumberOfReviews = scrapy.Field()
    # Description = scrapy.Field()
