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
    value_elements = []
    value_element_groups = []

    for tag in soup.find_all():
        elements.add(tag.name)

        # Find element groups
        element_group = [tag.name]
        if tag.attrs:
            attribute_names = sorted(tag.attrs.keys())
            element_group.extend(attribute_names)
        element_groups.append(', '.join(element_group))

        # Find elements with values
        value_element = f"{tag.name}: {tag.string}"
        value_elements.append(value_element)

        # Find element groups with values
        value_element_group = f"{', '.join(element_group)}: {tag.string}"
        value_element_groups.append(value_element_group)

    return list(elements), list(element_groups), value_elements, value_element_groups



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
            for attribute in tag.attrs:
                attributes.add(attribute)

                # Find attribute groups
                attribute_group = [attribute]
                attribute_group.extend(sorted(tag.attrs.keys()))
                attribute_groups.append(', '.join(attribute_group))

    return list(attributes), list(attribute_groups)

def scrape_with_class(html_content, class_name, parser='html.parser'):
    soup = BeautifulSoup(html_content, parser)
    selected_elements = soup.find_all(class_=class_name)
    scraped_data = [element.prettify() for element in selected_elements]
    return scraped_data


def scrape_with_class_group(html_content, class_group, parser='html.parser'):
    soup = BeautifulSoup(html_content, parser)
    selected_elements = soup.find_all(class_=class_group.split(','))
    scraped_data = [element.get_text(strip=True) for element in selected_elements]
    return scraped_data

def scrape_with_class_helper(html_content, class_name):
    soup = BeautifulSoup(html_content, 'html.parser')
    selected_elements = soup.find_all(class_=class_name)
    scraped_data = [element.get_text(strip=True) for element in selected_elements]
    return scraped_data

def scrape_with_class_group_helper(html_content, class_group):
    soup = BeautifulSoup(html_content, 'html.parser')
    selected_elements = soup.find_all(class_=class_group.split(','))
    scraped_data = [element.get_text(strip=True) for element in selected_elements]
    return scraped_data


def scrape_with_element(html_content, element):
    soup = BeautifulSoup(html_content, 'html.parser')
    selected_elements = soup.find_all(element)
    scraped_data = [str(element) for element in selected_elements]
    return scraped_data

def scrape_with_tag(html_content, tag):
    soup = BeautifulSoup(html_content, 'html.parser')
    selected_elements = soup.find_all(tag)
    scraped_data = [str(element) for element in selected_elements]
    return scraped_data


def scrape_with_attribute(html_content, attribute):
    soup = BeautifulSoup(html_content, 'html.parser')
    selected_elements = soup.find_all(attrs={attribute: True})
    scraped_data = [str(element) for element in selected_elements]
    return scraped_data

def scrape_with_element_group(html_content, element_group):
    soup = BeautifulSoup(html_content, 'html.parser')
    selected_elements = soup.select(element_group)
    scraped_data = [str(element) for element in selected_elements]
    return scraped_data

def scrape_with_attribute_group(html_content, attribute_group):
    soup = BeautifulSoup(html_content, 'html.parser')
    selected_elements = soup.find_all(attrs=parse_attribute_group(attribute_group))
    scraped_data = [str(element) for element in selected_elements]
    return scraped_data

def parse_attribute_group(attribute_group):
    attributes = attribute_group.split(',')
    attribute_dict = {}
    for attribute in attributes:
        if '=' in attribute:
            key, value = attribute.split('=')
            attribute_dict[key.strip()] = value.strip()
    return attribute_dict

def scrape_with_tag_group(html_content, tag_group):
    soup = BeautifulSoup(html_content, 'html.parser')
    selected_elements = soup.select(tag_group)
    scraped_data = [str(element) for element in selected_elements]
    return scraped_data
