import url_checker
from url_checker import start_page_check
from parser import WebsiteParser

if __name__ == "__main__":
    url = url_checker.start_page_check()
    depth = 1
    parser = WebsiteParser.parse_website(url, depth)

    #parsed_links = parser.parse_website(url, depth)
