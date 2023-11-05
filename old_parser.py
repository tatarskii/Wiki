from bs4 import BeautifulSoup
from url_checker import html_get


class GetPageLinks:
    def __init__(self):
        self.links_dict = {}
        self.div_id = 'mw-content-text'
        self.div_class = 'reflist reflist-columns references-column-width'
        self.div_sup_id = 'reference'

    def find_links_in_div_with_id(self):
        bs = BeautifulSoup(html_get(), 'html.parser')
        link_list = []
        title_list = []

        try:
            # Find all links in body container
            finded_div = bs.find('div', id=self.div_id)

            if finded_div:
                for link in finded_div.find_all('a'):
                    url = link.get("href")
                    title = link.get("title")
                    if url not in link_list:
                        link_list.append(url)
                        title_list.append(title)

                return link_list, title_list

        except Exception as e:
            print(e)

    def find_ref_links(self):
        bs = BeautifulSoup(html_get(), 'html.parser')
        link_list = []
        title_list = []

        try:
            # Find links in reference col
            finded_class = bs.find('div', class_=self.div_class)

            if finded_class:
                for link in finded_class.find_all('a'):
                    url = link.get("href")
                    title = link.get("title")
                    if url not in link_list:
                        link_list.append(url)
                        title_list.append(title)

                return link_list, title_list

        except Exception as e:
            print(e)

    def find_ref_links_in_text(self):
        bs = BeautifulSoup(html_get(), 'html.parser')
        link_list = []
        title_list = []


        try:
            # Find reference link in body container
            finded_ref_sup = bs.find('sup', class_=self.div_sup_id)

            if finded_ref_sup:
                for link in finded_ref_sup.find_all('a'):
                    url = link.get("href")
                    title = link.get("title")
                    if title not in title_list:
                        link_list.append(url)
                        title_list.append(title)

                return link_list, title_list

        except Exception as e:
            print(e)

    def get_links_dict(self, div_class=None):
        if div_class is not None:
            self.div_id = div_class
        link_list, title_list = self.find_links_in_div_with_id()
        self.links_dict = {url: title for url, title in zip(link_list, title_list)}
        return self.links_dict

