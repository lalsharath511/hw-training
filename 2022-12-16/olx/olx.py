import csv

import scrapy
from scrapy.crawler import CrawlerProcess
import json

class Olx(scrapy.Spider):
    name = 'olx'
    url = 'https://www.olx.in/api/relevance/v2/search?category=1725&facet_limit=100&lang=en-IN&location=4058873&location_facet_limit=20&platform=web-desktop&size=40&user=18519013f0fx26431fa'
    headers={
        "user-agent": "Mozilla / 5.0 (X11; Linux x86_64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
    }
    def __int__(self):
        with open('results.csv', 'w') as csv_file:
            csv_file.write('title,discription,location,area,beds,bathrooms,total_sqft,price\n')
    def start_requests(self):
        for page in range(0, 450):
            yield scrapy.Request(url=self.url + "&page=" + str(page), headers=self.headers, callback=self.parse)



    def parse(self, res):
        data = res.text

        data = json.loads(data)

        for offer in data['data']:
            items = {
                'title': offer['title'],
                'discription': offer['description'].replace('\n', ' '),
                'location': offer['locations_resolved']['ADMIN_LEVEL_3_name'],
                'area': offer['locations_resolved']['SUBLOCALITY_LEVEL_1_name'],
                'beds': offer['main_info'].split("-")[0],
                'bathrooms': offer['main_info'].split("-")[1],
                'total_sqft': offer['main_info'].split("-")[2],
                'price': offer['price']['value']['display']

            }
            print(json.dumps(items, indent=2))
            with open('result.csv', 'a') as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=items.keys())
                writer.writerow(items)


process = CrawlerProcess()
process.crawl(Olx)
process.start()

#debug
# Olx.parse(Olx, '')