from bs4 import BeautifulSoup, Comment, CData, ProcessingInstruction, Declaration, Doctype
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

def scrape_website(url):
    # Scraping HTML using requests
    response = requests.get(url)
    html_requests = response.text
    
    # Scraping HTML using html.parser
    soup_html_parser = BeautifulSoup(html_requests, 'html.parser')
    html_html_parser = soup_html_parser.prettify()
    
    # Scraping HTML using lxml
    soup_lxml = BeautifulSoup(html_requests, 'lxml')
    html_lxml = soup_lxml.prettify()
    
    # Scraping HTML using lxml-xml
    soup_lxml_xml = BeautifulSoup(html_requests, 'lxml-xml')
    html_lxml_xml = soup_lxml_xml.prettify()
    
    # Scraping HTML using html5lib
    soup_html5lib = BeautifulSoup(html_requests, 'html5lib')
    html_html5lib = soup_html5lib.prettify()
    
    # Parsed tree design
    tree_design = soup_html_parser.prettify()
    
    # Sitemap
    sitemap = []
    for link in soup_html_parser.find_all('a', href=True):
        sitemap.append(link['href'])
    
    return {
        'HTML using requests': html_requests,
        'HTML using html.parser': html_html_parser,
        'HTML using lxml': html_lxml,
        'HTML using lxml-xml': html_lxml_xml,
        'HTML using html5lib': html_html5lib,
        'Parsed Tree Design': tree_design,
        'Sitemap': sitemap,
        'soup_html_parser': soup_html_parser,
        'soup_lxml': soup_lxml,
        'soup_lxml_xml': soup_lxml_xml, 
        'soup_html5lib': soup_html5lib,
    }
    

def scrape_html_file(url):
    # Create BeautifulSoup object
    #soup = soup_param
    response = requests.get(url)
    html_requests = response.text
    
    # Scraping HTML using html.parser
    soup = BeautifulSoup(html_requests, 'html.parser')
    # Scrape classes
    classes = [element.get('class') for element in soup.find_all(class_=True)]

    # Scrape elements
    elements = [element.name for element in soup.find_all()]

    # Scrape attributes
    attributes = [element.attrs for element in soup.find_all()]

    # Scrape multivalued attributes
    multivalued_attributes = [
        {key: value for key, value in element.attrs.items() if isinstance(value, list)}
        for element in soup.find_all()
    ]

    # Scrape tags
    tags = [element.name for element in soup.find_all()]

    # Scrape names
    names = [element.name for element in soup.find_all()]

    # Scrape NavigableStrings
    navigatable_strings = [element.string for element in soup.find_all(string=True) if isinstance(element, str)]

    # Scrape comments
    comments = [element.string for element in soup.find_all(string=lambda text: isinstance(text, Comment))]

    # Scrape CDATA
    cdata = [element.string for element in soup.find_all(string=lambda text: isinstance(text, CData))]

    # Scrape processing instructions
    processing_instructions = [element.string for element in soup.find_all(string=lambda text: isinstance(text, ProcessingInstruction))]

    # Scrape declarations
    declarations = [element.string for element in soup.find_all(string=lambda text: isinstance(text, Declaration))]

    # Scrape doctypes
    doctypes = [element.string for element in soup.find_all(string=lambda text: isinstance(text, Doctype))]

    # Scrape .contents
    contents = [element.contents for element in soup.find_all()]

    # Scrape .children
    children = [list(element.children) for element in soup.find_all()]

    # Scrape .descendants
    descendants = [list(element.descendants) for element in soup.find_all()]

    # Scrape .string
    strings = [element.string for element in soup.find_all()]

    # Scrape .stripped_strings
    stripped_strings = [list(element.stripped_strings) for element in soup.find_all()]

    # Scrape .parent
    parents = [element.parent.name if element.parent else None for element in soup.find_all()]

    # Scrape .parents
    parents_hierarchy = [[parent.name for parent in element.parents] if element.parents else [] for element in soup.find_all()]

    # Scrape .next_sibling
    next_siblings = [element.next_sibling.name if element.next_sibling else None for element in soup.find_all()]

    # Scrape .previous_sibling
    previous_siblings = [element.previous_sibling.name if element.previous_sibling else None for element in soup.find_all()]

    # Scrape .next_siblings
    next_siblings_hierarchy = [[sibling.name for sibling in element.next_siblings] if element.next_siblings else [] for element in soup.find_all()]

    # Scrape .previous_siblings
    previous_siblings_hierarchy = [[sibling.name for sibling in element.previous_siblings] if element.previous_siblings else [] for element in soup.find_all()]

    # Scrape .next_element
    next_elements = [element.next_element.name if element.next_element else None for element in soup.find_all()]

    # Scrape .previous_element
    previous_elements = [element.previous_element.name if element.previous_element else None for element in soup.find_all()]

    # Scrape .next_elements
    next_elements_hierarchy = [[next_element.name for next_element in element.next_elements] if element.next_elements else [] for element in soup.find_all()]

    # Scrape .previous_elements
    previous_elements_hierarchy = [[previous_element.name for previous_element in element.previous_elements] if element.previous_elements else [] for element in soup.find_all()]

    # Scrape string filter
    def string_filter(element):
        return element.string.strip() == 'Text'

    string_filter_results = [element for element in soup.find_all(string=string_filter)]

    # Scrape regex filter
    import re

    def regex_filter(element):
        return re.match(r'^[0-9]+$', element.string)

    regex_filter_results = [element for element in soup.find_all(string=regex_filter)]

    # Scrape list filter
    list_filter_results = soup.find_all(string=['Text 1', 'Text 2'])

    # Scrape true filter
    true_filter_results = soup.find_all(lambda tag: True)

    # Scrape a function filter
    def filter_function(tag):
        # Custom filtering logic
        return True

    function_filter_results = soup.find_all(filter_function)

    # Scrape find_all
    find_all_results = soup.find_all()

    # Scrape name argument
    name_argument_results = soup.find_all(name='tag_name')

    # Scrape keyword argument
    keyword_argument_results = soup.find_all(attr_name='attr_value')

    # Scrape search by CSS class
    search_by_css_class_results = soup.find_all(class_='class_name')

    # Scrape string argument
    string_argument_results = soup.find_all(string='text')

    # Scrape limit argument
    limit_argument_results = soup.find_all(limit=10)

    # Scrape recursive argument
    recursive_argument_results = soup.find_all(recursive=True)

    # Scrape CSS selectors
    css_selectors_results = soup.select('selector1, selector2, selector3')

    return {
        'Classes': classes,
        'Elements': elements,
        'Attributes': attributes,
        'Multivalued Attributes': multivalued_attributes,
        'Tags': tags,
        'Names': names,
        'NavigatableStrings': navigatable_strings,
        'Comments': comments,
        'CDATA': cdata,
        'Processing Instructions': processing_instructions,
        'Declarations': declarations,
        'Doctypes': doctypes,
        'Contents': contents,
        'Children': children,
        'Descendants': descendants,
        'Strings': strings,
        'Stripped Strings': stripped_strings,
        'Parents': parents,
        'Parents Hierarchy': parents_hierarchy,
        'Next Sibling': next_siblings,
        'Previous Sibling': previous_siblings,
        'Next Siblings Hierarchy': next_siblings_hierarchy,
        'Previous Siblings Hierarchy': previous_siblings_hierarchy,
        'Next Element': next_elements,
        'Previous Element': previous_elements,
        'Next Elements Hierarchy': next_elements_hierarchy,
        'Previous Elements Hierarchy': previous_elements_hierarchy,
        'String Filter': string_filter_results,
        'Regex Filter': regex_filter_results,
        'List Filter': list_filter_results,
        'True Filter': true_filter_results,
        'Function Filter': function_filter_results,
        'find_all': find_all_results,
        'Name Argument': name_argument_results,
        'Keyword Argument': keyword_argument_results,
        'Search by CSS Class': search_by_css_class_results,
        'String Argument': string_argument_results,
        'Limit Argument': limit_argument_results,
        'Recursive Argument': recursive_argument_results,
        'CSS Selectors': css_selectors_results
    }
