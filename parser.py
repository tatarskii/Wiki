import requests
import url_checker
from bs4 import BeautifulSoup
import json


class WebsiteParser:
    def __init__(self):

        self.class_names = ['mw-redirect', None]
        self.sub_class = ['reference', 'mw-hidden-catlinks', 'extiw']

    def parse_website(self, url, depth):  # DO NOT CHANGE DEPTH!!!
        print(f"Starting to parse {url} at depth {depth}")


        try:
            response = requests.get(url)
            bs = BeautifulSoup(response.text, 'html.parser')

            # Find the div with id "bodyContent"
            body_div = bs.find('div', id='bodyContent')

            def custom_filter(tag):
                if (
                        tag.name == 'a' and
                        ('class' in tag.attrs and any(cls in tag['class'] for cls in self.class_names))
                        or ('class' in tag.attrs and any(cls in tag['class'] for cls in ['another_class']))
                        or ('class' not in tag.attrs)
                ):
                    # Exclude links
                    if (tag.find('sup', class_=self.sub_class)
                            or ('extiw' in tag.get('class', [])
                                or ('This article is semi-protected.' in tag.get('title', [])))):
                        return False

                    # Exclude links by parent div
                    mw_hidden_catlinks_div = tag.find_parent('div', id='mw-hidden-catlinks')
                    if mw_hidden_catlinks_div is not None:
                        return False

                    navigation_div = tag.find_parent('div', role='navigation')
                    if navigation_div is not None:
                        return False

                    # Exclude links by start of the url
                    if (
                            tag.get('href', '').startswith('#cite')
                            or tag.get('href', '').startswith('/wiki/Portal:')
                            or tag.get('href', '').startswith('/wiki/Help:')
                            or tag.get('href', '').startswith('/wiki/Category:')
                            or tag.get('href', '').startswith('/wiki/Special:')
                            or tag.get('href', '').startswith('mw-data:')
                            or tag.get('href', '').startswith('https://en.wikipedia.org/w/index.php')

                    ):
                        return False

                    return True
                return False

            filtered_links = body_div.find_all(custom_filter)

            # Create a dict of {href: title} for found links
            links_dict = {link.get('href', ''): link.get('title', '') for link in filtered_links}

            if depth > 1:
                new_links = {}
                for link in list(links_dict.keys()):
                    if link.startswith('/wiki'):
                        child_url = 'https://en.wikipedia.org' + link
                        new_links[link] = self.parse_website(child_url, depth - 1)
                links_dict.update(new_links)

            return links_dict

        except requests.RequestException as e:
            print('An error occurred while making the request:', str(e))
            return {}


website_parser = WebsiteParser()
parsed_links = website_parser.parse_website()

with open('parsed_links.json', 'w') as f:
    json.dump(parsed_links, f)

for href, title in parsed_links.items():
    print(f'Link: {href}, Title: {title}')
