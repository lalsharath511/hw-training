import requests
from parsel import Selector
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.selector import Selector


class Alliebeth(scrapy.Spider):
    # scraper name
    name = 'alliebeth'
    
    # headers
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-user': '?1',
        }
    
    # custom settings
    custom_settings = {
        'CONCURRENT_REQUEST_PER_DOMAIN': 10,
    }

    # general crawler
    def start_requests(self):
       
        
        
        # loop over list of initial links to crawl
         
            # initial HTTP request
        link='https://www.alliebeth.com/associates/int/'
        yield scrapy.Request(
            url=link,
            headers=self.headers,
            callback=self.parse_pagination
        )
            #break
            
    # parse pagination
    def parse_pagination(self, response):        
        
               
        
        # loop over the range of pages
        for page in range(1, 2):
            # generate next page URL
            next_page = f'https://www.alliebeth.com/associates/int/{page}-pg'
            
           
            # crawl next page
            yield response.follow(
                url=next_page,
                headers=self.headers,
                dont_filter=True,
                callback=self.parse_links
            )
            
            #break
        
    # parse links
    def parse_links(self, response):
       
      
        # loop over property cards
        for card_url in response.xpath('//a[@class="url"]/@href'):
            # crawl next listing
            yield response.follow(
                url=card_url.extract(),
                headers=self.headers,
                callback=self.parse_listing
            )
            #break
      
        
    # parse listing
    def parse_listing(self, response):
        # extract features
        
        features = {
            'name': response.xpath('//h1[@class="u-block  agent-details__name"]/text()').extract(),
            'url': response.url,
            'city': '',
            
            'country': '',
            
            'first_name': '',

            'middle_name': '',
            
            'last_name': '',

            'image_url': [],

            'title': [],
                                    
            'office_name': [],
                           
            'description': [],
            
            'address': [],
             'city' :'' ,
            'zipcode':'' ,_
            'state': ,
            'agent_phone_numbers': ,
            'office_phone_numbers': ,
            'social': social
            'website' : website
            'email': ''
            'profile_url'] = url
        }
          
        
        print(features)
        
        # print(json.dumps(features, indent=2))
        
        # # write data to JSONL file
        # with open(self.filename, 'a') as f:
        #     f.write(json.dumps(features)  + '\n')
    
# main driver
if __name__ == '__main__':
  
    process = CrawlerProcess()
    process.crawl(ResidentialSale)
    process.start()
    
# class Allman:
#     def __init__(self):
#         self.headers = {
#         'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#         'accept-encoding': 'gzip, deflate, br',
#         'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
#         'upgrade-insecure-requests': '1',
#         'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
#         'sec-fetch-dest': 'document',
#         'sec-fetch-mode': 'navigate',
#         'sec-fetch-site': 'cross-site',
#         'sec-fetch-user': '?1',
#         }
#     def parse_link(self,url):
#         response = requests.get(url=url, headers=self.headers)
#         print(response.status_code)
#         selector = Selector(response.text)
#         names = selector.xpath('//a[@class="url"]/@href').extract()
#         print(names)
# url = 'https://www.alliebeth.com/associates/int/2-pg'
# allman = Allman()
# allman.parse_link(url)
