import requests
from parsel import Selector
import json

class Expreality():
    def __init__(self):
        self.headers = {
        "content-type": "application/json",
        "origin": "https://exprealty.com",
        "referer": "https://exprealty.com/",
        "sec-ch-ua": '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': "Linux",
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
		'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
		} 
        self.payload={"operationName":"SearchQuery",
                      "variables":{"searchType":"AGENT","name":"a","country":"US","pagination":{"size":24,"from":0},"sort": None,},
                      "query":"fragment SearchResultFragment on SearchResult {  agents {    activeLocations {     city      state      __typename    }    asab    bio    cityState    email    facebook    firstName    id    lastName    linkedIn    phoneNumber    photo    state    stateBroker    preferredName    title    twitter    website    __typename  }  count  __typename}query SearchQuery($country: String, $location: String, $name: String, $pagination: Pagination, $searchType: SearchType!, $sort: Sort) {  search(    country: $country    location: $location    name: $name    pagination: $pagination    searchType: $searchType    sort: $sort  ) {    ...SearchResultFragment    __typename  }}"}
                      
    def parse(self, url,):
        response = requests.post(url, headers=self.headers,data=json.dumps(self.payload))
        data=response.text
        data = json.loads(data)
        # print(type(response))
        # data1=response["data"]
        # print(data)
        # `['0']
        # data=data['data']
        # data=data["search"`]
        count=0
        for agents in data['data']['search']['agents']:
            print(agents["activeLocations"]["city"])
            break
            details = {
                'country': 'United states',
                'first_name': first_name,
                'middle_name': middle_name,
                'last_name': last_name,
                'image_url': image_url,
                'title': title,
                'office_name': office,
                'description': disc,
                'languages': [],
                'address': address,
                'city': city,
                'zip_code': zip_code,
                'state': state,
                'agent_phone': agent_phone,
                'office_phone': "",
                'social': "",
                'website': website,
                'agent_email':  agent_email,
                'profile_url': url,
                }
        
        print(response.status_code)
        print()
url = 'https://agentdir-api.showcaseidx.com/graphql'
ebby = Expreality()
ebby.parse(url)
                