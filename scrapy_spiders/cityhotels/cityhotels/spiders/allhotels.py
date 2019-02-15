# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider
from scrapy.loader import ItemLoader
from cityhotels.items import CityhotelsItem

class AllhotelsSpider(scrapy.Spider):
    name = 'allhotels'
    allowed_domains = ['booking.com']
    start_urls = ['https://www.booking.com']
    #handle_httpstatus_list = [301, 302]
    def parse(self, response):
        # page_hotels = response.xpath('.//*[@data-et-view=" eWHJbWPNZWEHXT:5"]')
        page_hotels = response.xpath('.//*[@class="rlp-main-hotel__info"]')
        for ahotel in page_hotels:
            Urls = ahotel.xpath('.//*/@href').extract()
            #hotel_id = ahotel.xpath('.//@data-hotelid').extract_first()
            # hotel_name = ahotel.xpath('.//*[@class="sr-hotel__name\n"]/text()').extract_first().replace('\n','')
            hotel_name = ahotel.xpath('.//*[@target="_blank"]/text()').extract_first()
            # hotel_url = ahotel.xpath('.//*[@class="hotel_name_link url"]/@href').extract_first().replace('\n','')
            hotel_url = response.urljoin(Urls[0])
            rev_url = response.urljoin(Urls[-1])
            # full_hotel_url = 'https://www.booking.com'+str(hotel_url)
            # rev_score = ahotel.xpath('.//*[@class="bui-review-score__badge"]/text()').extract_first()#.replace(' ','')
            # num_of_score = ahotel.xpath('.//*[@class="bui-review-score__text"]/text()').extract_first()#.replace(' ','')

            l = ItemLoader(item=CityhotelsItem(), selector=response)
            # l.add_value('HotelID',hotel_id)
            l.add_value('HotelName',hotel_name)
            l.add_value('HotelUrl',hotel_url)
            l.add_value('HotelReviewUrl',rev_url)
            # l.add_value('ReviewScore',rev_score)
            # l.add_value('NumberOfReviews',num_of_score)
            yield l.load_item()

        # next_page = response.xpath('.//*[@class="bui-pagination__item bui-pagination__next-arrow"]/a/@href').extract_first()
        next_page = response.xpath('.//*[@class="rlp-main-pagination__btn-txt--next"]/@href').extract_first()
        if next_page is not None:
            next_page_url = response.urljoin(next_page)
            yield scrapy.Request(next_page_url, callback=self.parse)
