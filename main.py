import requests
from bs4 import BeautifulSoup
import re


class Parser:

    def __init__(self):
        pass

    def zero_page(self):

        wiki_url = input("Paste your link here: ")
        try:
            re.match("(https?://en\\.wikipedia\\.org/wiki/([a-zA-Z]|[0-9]))", wiki_url)
            response = requests.get(wiki_url)
            if response:
                return response.text
        except Exception as e:
            print(e)

    def pars(self):
        bs = BeautifulSoup(self.zero_page(), 'html.parser')
        link_list = []
        try:
            for link in bs.find_all('a'):
                url = link.get("href")
                if url not in link_list:
                    link_list.append(url)
            return link_list
        except Exception as e:
            print(e)

    def bd_connect(self):
        pass

    def bd_create(self):
        pass

    def bd_write(self):
        pass


tmp = Parser()
for i in tmp.pars():
    print(i)
