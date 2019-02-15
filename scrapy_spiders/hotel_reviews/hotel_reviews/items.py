# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HotelReviewsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    HotelName = scrapy.Field()
    UserName = scrapy.Field()
    UserCountry = scrapy.Field()
    NumReviewGiven = scrapy.Field()
    UserAgeGroup = scrapy.Field()
    Heading = scrapy.Field()
    NegativeReview = scrapy.Field()
    PositiveReview = scrapy.Field()
    SelfTag = scrapy.Field()
    StayDate = scrapy.Field()
    GivenScore = scrapy.Field()
    Cleanliness = scrapy.Field()
    Comfort = scrapy.Field()
    Location = scrapy.Field()
    Facilities = scrapy.Field()
    Staff = scrapy.Field()
    ValueForMoney = scrapy.Field()
    FreeWifi = scrapy.Field()
