import requests
import re


class UrlCheck:
    def start_page_check(self):

        wiki_url = input("Paste your link here: ")
        try:
            re.match("(https?://en\\.wikipedia\\.org/wiki/([a-zA-Z]|[0-9]))", wiki_url)
            return str(wiki_url)
        except Exception as e:
            print(e)

    def html_get(self):
        response = requests.get(self.start_page_check())
        if response:
            return response.text


tmp = UrlCheck()
