# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider
from scrapy.loader import ItemLoader
from hotel_info.items import HotelInfoItem

class HotelDetailsSpider(scrapy.Spider):
    name = 'hotel_details'
    allowed_domains = ['booking.com']
    start_urls = ['http://booking.com/']

    def parse(self, response):
        # hxs = HtmlXPathSelector(response)
        # if not hxs.select('.//*[@class="show_all_reviews_btn"]/@href'):
        #     yield Request(url=response.url, dont_filter=True)

        hotel_id = response.xpath('//*[@name="hotel_id"]/@value').extract_first()
        hotel_name = response.xpath('//*[@class="hp__hotel-name"]/text()').extract()[1].replace('\n','')
        # all_review_url = response.xpath('.//*[@class="show_all_reviews_btn"]/@href').extract_first()
        #review_url = "https://booking.com"+str(all_review_url)
        # hotel_address = response.xpath('.//*[@class="address address_clean"]/span/text()').extract()[2].replace('\n','')
        hotel_coord = response.xpath('.//*[@class="address address_clean"]/a/@data-coords').extract_first()
        all_facilities = response.xpath('.//*[@class="facilitiesChecklistSection"]/ul/li/span/text()').extract()
        all_facilities = [x.replace('\n','') for x in all_facilities]
        important_facility = response.xpath('.//*[@class="important_facility "]/@data-name-en').extract()
        image_urls = response.xpath('.//*[@class="b_nha_hotel_small_images hp_thumbgallery_with_counter"]/a/@href').extract()

        l = ItemLoader(item=HotelInfoItem(), selector=response)
        l.add_value('HotelID',hotel_id)
        l.add_value('HotelName',hotel_name)
        # l.add_value('HotelAddress',hotel_address)
        l.add_value('HotelCoordinate',hotel_coord)
        # l.add_value('ReviewUrl',all_review_url)
        l.add_value('MainFacilities',important_facility)
        l.add_value('Facilities',all_facilities)
        l.add_value('ImageUrls',image_urls)
        yield l.load_item()
