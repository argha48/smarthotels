# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider
from scrapy.loader import ItemLoader
from hotel_reviews.items import HotelReviewsItem

class HotelReviewSpider(scrapy.Spider):
    name = 'hotel-review'
    allowed_domains = ['booking.com']
    start_urls = ['http://booking.com/']

    def parse(self, response):
        hotel_name = response.xpath('.//*[@class="item hotel_name"]/a/text()').extract_first()
        hotel_score = response.xpath('.//*[@class="c-score-bar__score"]/text()').extract()
        hotel_clean = response.xpath('.//*[@data-question="hotel_clean"]/*[@class="review_score_value"]/text()').extract_first()
        hotel_comfort = response.xpath('.//*[@data-question="hotel_comfort"]/*[@class="review_score_value"]/text()').extract_first()
        hotel_location = response.xpath('.//*[@data-question="hotel_location"]/*[@class="review_score_value"]/text()').extract_first()
        hotel_services = response.xpath('.//*[@data-question="hotel_services"]/*[@class="review_score_value"]/text()').extract_first()
        hotel_staff = response.xpath('.//*[@data-question="hotel_staff"]/*[@class="review_score_value"]/text()').extract_first()
        hotel_value = response.xpath('.//*[@data-question="hotel_value"]/*[@class="review_score_value"]/text()').extract_first()
        hotel_wifi = response.xpath('.//*[@data-question="hotel_wifi"]/*[@class="review_score_value"]/text()').extract_first()
        allreviewsinpage = response.xpath('.//*[@itemprop="review"]')
        for eachreview in allreviewsinpage:
            username = eachreview.xpath('.//p[@class="reviewer_name"]/*[@itemprop="name"]/text()').extract_first()
            usercountry = eachreview.xpath('.//*[@itemprop="nationality"]/*[@itemprop="name"]/text()').extract_first()
            numreviewgiven = eachreview.xpath('.//*[@class="review_item_user_review_count"]/text()').extract_first()
            useragegroup = eachreview.xpath('.//*[@class="user_age_group"]/text()').extract_first()
            heading = eachreview.xpath('.//*[@class="review_item_header_content\n"]/*[@itemprop="name"]/text()').extract_first()
            neg_rev = eachreview.xpath('.//p[@class="review_neg "]/*[@itemprop="reviewBody"]/text()').extract_first()
            pos_rev = eachreview.xpath('.//p[@class="review_pos "]/*[@itemprop="reviewBody"]/text()').extract_first()
            tagging = eachreview.xpath('.//ul[@class="review_item_info_tags"]/*[@class="review_info_tag "]/text()').extract()
            stayedin = eachreview.xpath('.//p[@class="review_staydate "]/text()').extract_first()
            givenscore = eachreview.xpath('.//span[@class="review-score-badge"]/text()').extract_first()

            l = ItemLoader(item=HotelReviewsItem(), selector=response)
            l.add_value('HotelName',hotel_name)
            l.add_value('UserName',username)
            l.add_value('UserCountry',usercountry)
            l.add_value('NumReviewGiven',numreviewgiven)
            l.add_value('UserAgeGroup',useragegroup)
            l.add_value('Heading',heading)
            l.add_value('NegativeReview',neg_rev)
            l.add_value('PositiveReview',pos_rev)
            l.add_value('SelfTag',tagging)
            l.add_value('StayDate',stayedin)
            l.add_value('GivenScore',givenscore)
            l.add_value('Cleanliness',hotel_clean)
            l.add_value('Comfort',hotel_comfort)
            l.add_value('Location',hotel_location)
            l.add_value('Facilities',hotel_services)
            l.add_value('Staff',hotel_staff)
            l.add_value('ValueForMoney',hotel_value)
            l.add_value('FreeWifi',hotel_wifi)
            yield l.load_item()
            
        next_page = response.xpath('.//*[@class="page_link review_next_page"]/a/@href').extract_first()
        if next_page is not None:
            next_page_url = response.urljoin(next_page)
            yield scrapy.Request(next_page_url, callback=self.parse)
