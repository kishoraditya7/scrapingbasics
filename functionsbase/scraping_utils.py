from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse
import re

def check_robots_txt(url):
    response = requests.get(url + '/robots.txt')
    return response.status_code == 200

def scrape_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return None

def scrape_url_bs4_htmlparser(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup.prettify()
    return None

def scrape_url_bs4_lxml(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'lxml')
        return soup.prettify()
    return None

def scrape_url_bs4_html5lib(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html5lib')
        return soup.prettify()
    return None

def get_base_url(url):
    parsed_url = urlparse(url)
    base_url = parsed_url.scheme + '://' + parsed_url.netloc
    return base_url

def get_parse_tree(html_content, parser='html.parser'):
    soup = BeautifulSoup(html_content, parser)
    parse_tree = soup.prettify()
    return parse_tree

def scrape_all_classes(html_content, parser='html.parser'):
    soup = BeautifulSoup(html_content, parser)
    classes = set()
    class_groups = []

    for tag in soup.find_all(class_=True):
        tag_classes = tag.attrs.get('class')
        classes.update(tag_classes)

        # Find class attributes with multiple classes
        if tag_classes:
            class_groups.append(', '.join(tag_classes))

    return list(classes), list(class_groups)

def scrape_all_elements(html_content, parser='html.parser'):
    soup = BeautifulSoup(html_content, parser)
    elements = set()
    element_groups = []

    for tag in soup.find_all():
        elements.add(tag.name)

        # Find element groups
        element_group = [tag.name]
        if tag.attrs:
            attribute_names = sorted(tag.attrs.keys())
            element_group.extend(attribute_names)
        element_groups.append(', '.join(element_group))
    return list(elements), list(element_groups)


def scrape_all_tags(html_content, parser='html.parser'):
    soup = BeautifulSoup(html_content, parser)
    tags = set()
    tag_groups = []

    for tag in soup.find_all():
        tags.add(tag.name)

        # Find tag groups
        tag_group = [tag.name]
        if tag.attrs:
            attribute_names = sorted(tag.attrs.keys())
            tag_group.extend(attribute_names)
        tag_groups.append(', '.join(tag_group))

    return list(tags), list(tag_groups)


def scrape_all_attributes(html_content, parser='html.parser'):
    soup = BeautifulSoup(html_content, parser)
    attributes = set()
    attribute_groups = []

    for tag in soup.find_all():
        if tag.attrs:
            attributes.update(tag.attrs.keys())

            # Find attribute groups
            attribute_group = sorted(tag.attrs.keys())
            attribute_groups.append(', '.join(attribute_group))

    return list(attributes), list(attribute_groups)