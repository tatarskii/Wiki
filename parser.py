from bs4 import BeautifulSoup
from url_checker import html_get


class Parser:

    def pars(self):
        bs = BeautifulSoup(html_get(), 'html.parser')
        link_list = []
        try:
            for link in bs.find_all('a'):
                url = link.get("href")
                if url not in link_list:
                    link_list.append(url)
            return link_list
        except Exception as e:
            print(e)
