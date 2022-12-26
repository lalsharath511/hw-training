import scrapy

class QuotesSpider(scrapy.Spider):
    name ="quotes"
    
    def start_requests(self):
        urls=[
            'https://quotes.toscrape.com/page/1/'
        ]