from bs4 import BeautifulSoup
from url_checker import html_get


class GetPageLinks:

    def get_links_list(self):
        bs = BeautifulSoup(html_get(), 'html.parser')
        link_list = []
        title_list = []

        try:
            for link in bs.find_all('a'):
                url = link.get("href")
                title = link.get("title")
                if url not in link_list:
                    link_list.append(url)
                    title_list.append(title)
            return link_list, title_list
        except Exception as e:
            print(e)

    def get_links_dict(self):
        link_list, title_list = self.get_links_list()
        links_dict = {url: title for url, title in zip(link_list, title_list)}
        return links_dict


