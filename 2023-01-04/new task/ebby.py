# import scrapy
# from scrapy.crawler import CrawlerProcess
# import json

# class Olx(scrapy.Spider):
#     name = 'ebby'
#     url = 'https://www.ebby.com/CMS/CmsRoster/RosterSection?layoutID=956&pageSize=10&pageNumber=4&sortBy=officename'
#     headers={
#         "Host": "www.ebby.com",
#         "Referer": "https://www.ebby.com/roster/offices",
#         "sec-ch-ua-platform": "Linux",
#         "Sec-Fetch-Dest": "empty",
#         "Sec-Fetch-Mode": "cors",
#         "Sec-Fetch-Site": "same-origin",
#         "user-agent": "Mozilla / 5.0 (X11; Linux x86_64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
#     }
#     def __int__(self):
#         # with open('results.csv', 'w') as csv_file:
#         #     csv_file.write('title,discription,location,area,beds,bathrooms,total_sqft,price\n')
#         pass
#     def start_requests(self):
#         # for page in range(0, 450):
#         response = scrapy.Requests.get(url=self.url, headers=self.headers)
#         print(response.status_code)
#         yield scrapy.Request(url=self.url, headers=self.headers, callback=self.parse)



#     def parse(self, res):
#         data = res.text
#         print(data)

#         # data = json.loads(data)

#         # for offer in data['data']:
#         #     items = {
#         #         'title': offer['title'],
#         #         'discription': offer['description'].replace('\n', ' '),
#         #         'location': offer['locations_resolved']['ADMIN_LEVEL_3_name'],
#         #         'area': offer['locations_resolved']['SUBLOCALITY_LEVEL_1_name'],
#         #         'beds': offer['main_info'].split("-")[0],
#         #         'bathrooms': offer['main_info'].split("-")[1],
#         #         'total_sqft': offer['main_info'].split("-")[2],
#         #         'price': offer['price']['value']['display']

#         #     }
#         #     print(json.dumps(items, indent=2))
#         #     with open('result.csv', 'a') as csv_file:
#         #         writer = csv.DictWriter(csv_file, fieldnames=items.keys())
#         #         writer.writerow(items)


# process = CrawlerProcess()
# process.crawl(Olx)
# process.start()

from parsel import Selector
import requests

class ExprealtyScraper:

    def __init__(self):
        self.headers = {
        "Host": "www.ebby.com",
        "Referer": "https://www.ebby.com/roster/offices",
        "sec-ch-ua-platform": "Linux",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "user-agent": "Mozilla / 5.0 (X11; Linux x86_64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
        
    def exprealty(self, url, ):
        response = requests.get(url=url, headers=self.headers)
        # print(response.text)
        if response.status_code != 200:
            raise Exception('Failed to load page')
        selector = Selector(text=response.text)
        # print(response.text)
        a=selector.xpath('//article[contains(@class,"rng-agent-roster-agent-card js-sort-item")]/a/@href')
        print(a)
        # for link in selector.xpath('//article[contains(@class,"rng-agent-roster-agent-card js-sort-item")]/a/@href'):
        #     print(link.text)
        
url = 'https://www.ebby.com/CMS/CmsRoster/RosterSection?layoutID=956&pageSize=10&pageNumber=4&sortBy=officename'
obj = ExprealtyScraper()
obj.exprealty(url)


