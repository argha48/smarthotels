from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

process = CrawlerProcess(get_project_settings())
# StartUrl_NewYork = ['https://www.booking.com/reviews/region/new-york-state.html?']
StartUrl_California = ['https://www.booking.com/reviews/region/california.html?']
# StartUrl_Miami = ['https://www.booking.com/reviews/us/city/miami.html?aid=356980;label=gog235jc-1DCCoo7AE4gANIM1gDaKcCiAEBmAExuAEHyAEM2AED6AEB-AECiAIBqAID;sid=0d08bf722a5ddd2919f937bec98b801b;']
# StartUrl_Florida = ['https://www.booking.com/reviews/region/florida.en-gb.html?']
process.crawl('allhotels', domain='booking.com', start_urls = StartUrl_California)
process.start()
