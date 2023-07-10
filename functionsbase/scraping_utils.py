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


