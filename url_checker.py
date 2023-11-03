import requests
import re


def start_page_check():

    wiki_url = input("Paste your link here: ")
    try:
        re.match("(https?://en\\.wikipedia\\.org/wiki/([a-zA-Z]|[0-9]))", wiki_url)
        return str(wiki_url)
    except Exception as e:
        print(e)


def html_get():
    response = requests.get(start_page_check())
    if response:
        return response.text


class UrlCheck:
    pass


tmp = UrlCheck()
