import csv
import scrapy
import json

class Meesho(scrapy.Spider):
    name = 'meesho'
    url = 'https://www.meesho.com/accessories-men/pl/3tp'
    headers={
        "user-agent": "Mozilla / 5.0 (X11; Linux x86_64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
    }
    
    def start_requests(self):
        yield scrapy.Request(url=self.url, headers=self.headers, callback=self.parse)
    def parse(self, res):
        data=res.text
        print(data)
        
obj=Meesho
obj.start_requests()
        
#     def __int__(self):
#         with open('results.csv', 'w') as csv_file:
#             csv_file.write('title,discription,location,area,beds,bathrooms,total_sqft,price\n')
#     def start_requests(self):
#         for page in range(0, 450):
#             yield scrapy.Request(url=self.url + "&page=" + str(page), headers=self.headers, callback=self.parse)



#     def parse(self, res):
#         data = res.text

#         data = json.loads(data)

#         for offer in data['data']:
#             items = {
#                 'title': offer['title'],
#                 'discription': offer['description'].replace('\n', ' '),
#                 'location': offer['locations_resolved']['ADMIN_LEVEL_3_name'],
#                 'area': offer['locations_resolved']['SUBLOCALITY_LEVEL_1_name'],
#                 'beds': offer['main_info'].split("-")[0],
#                 'bathrooms': offer['main_info'].split("-")[1],
#                 'total_sqft': offer['main_info'].split("-")[2],
#                 'price': offer['price']['value']['display']

#             }
#             print(json.dumps(items, indent=2))
#             with open('result.csv', 'a') as csv_file:
#                 writer = csv.DictWriter(csv_file, fieldnames=items.keys())
#                 writer.writerow(items)


# process = CrawlerProcess()
# process.crawl(Olx)
# process.start()

#debug
# Olx.parse(Olx, '')