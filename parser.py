import requests
import url_checker
from bs4 import BeautifulSoup


class WebsiteParser:
    def __init__(self):

        self.class_names = ['mw-redirect', None]
        self.sub_class = ['reference', 'mw-hidden-catlinks', 'extiw']

    def parse_website(self):
        try:
            response = requests.get(url_checker.start_page_check())

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
                    # Exclude links that contain "self.sup_name"
                    if (tag.find('sup', class_=self.sub_class)
                            or ('extiw' in tag.get('class', [])
                            or ('This article is semi-protected.' in tag.get('title', [])))):
                        return False

                    # Exclude links in div_id = "mw-hidden-catlinks"
                    excluded_div = tag.find_parent('div', id='mw-hidden-catlinks')
                    if excluded_div is not None:
                        return False
                    return True
                return False

            filtered_links = body_div.find_all(custom_filter)

            # Create a dict of {href: title} for found links
            links_dict = {link.get('href', ''): link.get('title', '') for link in filtered_links}
            return links_dict



        except requests.RequestException as e:
            print('An error occurred while making the request:', str(e))
            return {}


website_parser = WebsiteParser()
parsed_links = website_parser.parse_website()

for href, title in parsed_links.items():
    print(f'Link: {href}, Title: {title}')
