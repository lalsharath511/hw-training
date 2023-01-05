
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.selector import Selector
import urllib
import json
import datetime

# property scraper class
class ResidentialSale(scrapy.Spider):
    # scraper name
    name = 'ebby.com'
    
    # headers
    headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"
    }
    
    # # custom settings
    # custom_settings = {
    #     'CONCURRENT_REQUEST_PER_DOMAIN': 2,
    #     'DOWNLOAD_DELAY': 1
    # }

    # general crawler
    def start_requests(self):
        # init filename
       
        # loop over list of initial links to crawl
        for link in range(1,200):
            links='https://www.ebby.com/roster/agents/33'
            # initial HTTP request
            yield scrapy.Request(
                url=link,
                callback=self.parse_links
            )
            #break
            
   
        
    # parse links
    def parse_links(self, response):
        # get current page
        #current_page = ...
        
        try:
            current_page = int(current_page)
        except:
            current_page = 1
        
        # print debug info
        print("Page %s | %s" % (current_page, response.meta.get('total_pages')))

        # extract property cards
        #cards = [...]
        https://www.ebby.com/CMS/CmsRoster/RosterSection?layoutID=956&pageSize=10&pageNumber=16
        '''
        # loop over property cards
        for card_url in cards:
            # crawl next listing
            yield response.follow(
                url=card_url,
                headers=self.headers,
                meta={
                    'filename': self.filename
                },
                callback=self.parse_listing
            )
            #break
        '''
        
    # parse listing
    def parse_listing(self, response):
        # extract features
        features = {
            'id': '',
            'url': response.url,
            'city': '',
            
            'title': '',
            
            'price': '',

            'address': '',
            
            'floor_area': '',

            'key_features': [],

            'amenities': [],
                                    
            'image_urls': [],
                           
            'full_description': [],
            
            'coordinates': [],
        }
        
        print(json.dumps(features, indent=2))
        
        # write data to JSONL file
        with open(self.filename, 'a') as f:
            f.write(json.dumps(features)  + '\n')
    
# main driver
if __name__ == '__main__':
    #import logging
    #from scrapy.utils.log import configure_logging
    #logging.disable(logging.CRITICAL)
    #configure_logging()

    # run scraper
    process = CrawlerProcess()
    process.crawl(ResidentialSale)
    process.start()