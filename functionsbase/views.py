from django.shortcuts import render
from django.http import HttpResponseRedirect
from .scraping_utils import (
    check_robots_txt,
    scrape_url,
    scrape_url_bs4_htmlparser,
    scrape_url_bs4_lxml,
    scrape_url_bs4_html5lib,
    get_base_url,
    get_parse_tree,
    scrape_all_classes,
    scrape_all_attributes,
    scrape_all_elements,
    scrape_all_tags,
    scrape_with_class, 
    scrape_with_class_group,
    scrape_with_class_helper,
    scrape_with_class_group_helper,
    scrape_with_tag as utils_scrape_with_tag,
    scrape_with_attribute as utils_scrape_with_attribute,
    scrape_with_element as utils_scrape_with_element,
    scrape_with_attribute_group as utils_scrape_with_attribute_group,
    scrape_with_element_group,
    parse_attribute_group,
    scrape_with_tag_group as utils_scrape_with_tag_group,
    scrape_website,
)

def index(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        return HttpResponseRedirect('/results/?url=' + url)
    
    return render(request, 'index.html')

def results(request):
    url = request.GET.get('url')
    base_url = get_base_url(url)
    robots_txt_url = base_url + '/robots.txt'
    has_robots_txt = check_robots_txt(base_url)
    robots_txt_content = scrape_url(robots_txt_url) if has_robots_txt else None
    html_content = scrape_url(url)
    html_content_htmlparser = scrape_url_bs4_htmlparser(url)
    html_content_lxml = scrape_url_bs4_lxml(url)
    html_content_html5lib = scrape_url_bs4_html5lib(url)

    parse_tree = get_parse_tree(html_content)
    classes, class_groups = scrape_all_classes(html_content)
    elements, element_groups, value_elements, value_element_groups = scrape_all_elements(html_content)
    tags, tag_groups = scrape_all_tags(html_content)
    attributes, attribute_groups = scrape_all_attributes(html_content)
    classes_url = f"/classes/?url={url}"
    elements_url = f"/elements/?url={url}"
    tags_url = f"/tags/?url={url}"
    attributes_url = f"/attributes/?url={url}"
    html_requests_url = f"/html_requests/?url={url}"
    html_html_parser_url = f"/html_html_parser/?url={url}"
    html_lxml_url = f"/html_lxml/?url={url}"
    html_lxml_xml_url = f"/html_lxml_xml/?url={url}"
    html_html5lib_url = f"/html_html5lib/?url={url}"
    tree_design_url = f"/tree_design/?url={url}"
    sitemap_url = f"/sitemap/?url={url}"
    
    return render(request, 'results.html', {
        'url': url,
        'has_robots_txt': has_robots_txt,
        'robots_txt_url': robots_txt_url,
        'robots_txt_content': robots_txt_content,
        'html_content': html_content,
        'html_content_htmlparser': html_content_htmlparser,
        'html_content_lxml': html_content_lxml,
        'html_content_html5lib': html_content_html5lib,
        'parse_tree': parse_tree,
        'classes_url': classes_url,
        'classes': classes,
        'class_groups': class_groups,
        'elements_url': elements_url,
        'tags_url': tags_url,
        'attributes_url': attributes_url,
        'elements': elements,
        'tags': tags,
        'attributes': attributes,
        'element_groups': element_groups,
        'tag_groups' : tag_groups,
        'attribute_groups':attribute_groups,
        'value_elements':value_elements, 
        'value_element_groups':value_element_groups,
        'html_requests_url': html_requests_url,
        'html_html_parser_url': html_html_parser_url,
        'html_lxml_url': html_lxml_url,
        'html_lxml_xml_url': html_lxml_xml_url,
        'html_html5lib_url': html_html5lib_url,
        'tree_design_url': tree_design_url,
        'sitemap_url': sitemap_url,
    })




def robots_txt(request):
    url = request.GET.get('url')
    base_url = get_base_url(url)
    robots_txt_url = base_url + '/robots.txt'
    robots_txt_content = scrape_url(robots_txt_url)
    
    return render(request, 'robots_txt.html', {
        'url': url,
        'robots_txt_content': robots_txt_content,
    })

def html_code(request):
    url = request.GET.get('url')
    html_content = scrape_url(url)
    
    return render(request, 'html_code.html', {
        'url': url,
        'html_content': html_content,
    })

def html_code_parser(request, parser):
    url = request.GET.get('url')
    html_content = None

    if parser == 'htmlparser':
        html_content = scrape_url_bs4_htmlparser(url)
    elif parser == 'lxml':
        html_content = scrape_url_bs4_lxml(url)
    elif parser == 'html5lib':
        html_content = scrape_url_bs4_html5lib(url)
    
    return render(request, 'html_code_parser.html', {
        'url': url,
        'html_content': html_content,
        'parser': parser.capitalize(),
    })

def parse_tree(request):
    url = request.GET.get('url')
    html_content = scrape_url(url)
    parse_tree = get_parse_tree(html_content)

    return render(request, 'parse_tree.html', {
        'url': url,
        'parse_tree': parse_tree,
    })

def classes(request):
    url = request.GET.get('url')
    html_content = scrape_url(url)
    classes, class_groups = scrape_all_classes(html_content)

    return render(request, 'classes.html', {
        'classes': classes,
        'class_groups': class_groups,
        'url': url,
    })
    
def elements(request):
    url = request.GET.get('url')
    html_content = scrape_url(url)
    elements, element_groups, value_elements, value_element_groups = scrape_all_elements(html_content)

    return render(request, 'elements.html', {
        'elements': elements,
        'element_groups': element_groups,
        'value_elements': value_elements,
        'value_element_groups': value_element_groups,
        'url': url,
    })

def tags(request):
    url = request.GET.get('url')
    html_content = scrape_url(url)
    tags, tag_groups = scrape_all_tags(html_content)

    return render(request, 'tags.html', {
        'tags': tags,
        'tag_groups': tag_groups,
        'url': url,
    })

def attributes(request):
    url = request.GET.get('url')
    html_content = scrape_url(url)
    attributes, attribute_groups = scrape_all_attributes(html_content)

    return render(request, 'attributes.html', {
        'attributes': attributes,
        'attribute_groups': attribute_groups,
        'url': url,
    })
    

def scrape_with_class(request):
    url = request.GET.get('url')
    class_name = request.GET.get('class_name')

    if url and class_name:
        html_content = scrape_url(url)
        if html_content:
            scraped_data = scrape_with_class_helper(html_content, class_name)
            return render(request, 'scrape_with_class.html', {
                'url': url,
                'class_name': class_name,
                'scraped_data': scraped_data,
            })

    return render(request, 'scrape_with_class.html', {
        'url': url,
        'class_name': class_name,
        'scraped_data': None,
    })


def scrape_with_class_group(request):
    url = request.GET.get('url')
    class_group = request.GET.get('class_group')

    if url and class_group:
        html_content = scrape_url(url)
        if html_content:
            scraped_data = scrape_with_class_group_helper(html_content, class_group)
            return render(request, 'scrape_with_class_group.html', {
                'url': url,
                'class_group': class_group,
                'scraped_data': scraped_data,
            })

    return render(request, 'scrape_with_class_group.html', {
        'url': url,
        'class_group': class_group,
        'scraped_data': None,
    })
    

def scrape_with_element(request):
    url = request.GET.get('url')
    element = request.GET.get('element')

    if url and element:
        html_content = scrape_url(url)
        if html_content:
            scraped_data = utils_scrape_with_element(html_content, element)
            return render(request, 'scrape_with_element.html', {
                'url': url,
                'element': element,
                'scraped_data': scraped_data,
            })

    return render(request, 'scrape_with_element.html', {
        'url': url,
        'element': element,
        'scraped_data': None,
    })

def scrape_with_tag(request):
    url = request.GET.get('url')
    tag = request.GET.get('tag')

    if url and tag:
        html_content = scrape_url(url)
        if html_content:
            scraped_data = utils_scrape_with_tag(html_content, tag)
            return render(request, 'scrape_with_tag.html', {
                'url': url,
                'tag': tag,
                'scraped_data': scraped_data,
            })

    return render(request, 'scrape_with_tag.html', {
        'url': url,
        'tag': tag,
        'scraped_data': None,
    })


def scrape_with_attribute(request):
    url = request.GET.get('url')
    attribute = request.GET.get('attribute')

    if url and attribute:
        html_content = scrape_url(url)
        if html_content:
            scraped_data = utils_scrape_with_attribute(html_content, attribute)
            return render(request, 'scrape_with_attribute.html', {
                'url': url,
                'attribute': attribute,
                'scraped_data': scraped_data,
            })

    return render(request, 'scrape_with_attribute.html', {
        'url': url,
        'attribute': attribute,
        'scraped_data': None,
    })


def scrape_with_element_group(request):
    url = request.GET.get('url')
    element_group = request.GET.get('element_group')

    if url and element_group:
        html_content = scrape_url(url)
        if html_content:
            scraped_data = scrape_with_element_group(html_content, element_group)
            return render(request, 'scrape_with_element_group.html', {
                'url': url,
                'element_group': element_group,
                'scraped_data': scraped_data,
            })

    return render(request, 'scrape_with_element_group.html', {
        'url': url,
        'element_group': element_group,
        'scraped_data': None,
    })
def scrape_with_attribute_group(request):
    url = request.GET.get('url')
    attribute_group = request.GET.get('attribute_group')

    if url and attribute_group:
        html_content = scrape_url(url)
        if html_content:
            scraped_data = utils_scrape_with_attribute_group(html_content, attribute_group)
            return render(request, 'scrape_with_attribute_group.html', {
                'url': url,
                'attribute_group': attribute_group,
                'scraped_data': scraped_data,
            })

    return render(request, 'scrape_with_attribute_group.html', {
        'url': url,
        'attribute_group': attribute_group,
        'scraped_data': None,
    })

def scrape_with_tag_group(request):
    url = request.GET.get('url')
    tag_group = request.GET.get('tag_group')

    if url and tag_group:
        html_content = scrape_url(url)
        if html_content:
            scraped_data = utils_scrape_with_tag_group(html_content, tag_group)
            return render(request, 'scrape_with_tag_group.html', {
                'url': url,
                'tag_group': tag_group,
                'scraped_data': scraped_data,
            })

    return render(request, 'scrape_with_tag_group.html', {
        'url': url,
        'tag_group': tag_group,
        'scraped_data': None,
    })

def scrape(request):
    url = request.GET.get('url')
    
    if url:
        data = scrape_website(url)
        return render(request, 'results.html', {
            'url': url,
            'data': data,
        })
    
    return render(request, 'index.html')

def html_requests(request):
    url = request.GET.get('url')
    scraped_data = scrape_website(url).get('HTML using requests')
    return render(request, 'html_requests.html', {'url': url, 'scraped_data': scraped_data})

def html_html_parser(request):
    url = request.GET.get('url')
    scraped_data = scrape_website(url).get('HTML using html.parser')
    return render(request, 'html_html_parser.html', {'url': url, 'scraped_data': scraped_data})

def html_lxml(request):
    url = request.GET.get('url')
    scraped_data = scrape_website(url).get('HTML using lxml')
    return render(request, 'html_lxml.html', {'url': url, 'scraped_data': scraped_data})

def html_lxml_xml(request):
    url = request.GET.get('url')
    scraped_data = scrape_website(url).get('HTML using lxml-xml')
    return render(request, 'html_lxml_xml.html', {'url': url, 'scraped_data': scraped_data})

def html_html5lib(request):
    url = request.GET.get('url')
    scraped_data = scrape_website(url).get('HTML using html5lib')
    return render(request, 'html_html5lib.html', {'url': url, 'scraped_data': scraped_data})

def tree_design(request):
    url = request.GET.get('url')
    scraped_data = scrape_website(url).get('Parsed Tree Design')
    return render(request, 'tree_design.html', {'url': url, 'scraped_data': scraped_data})

def sitemap(request):
    url = request.GET.get('url')
    scraped_data = scrape_website(url).get('Sitemap')
    return render(request, 'sitemap.html', {'url': url, 'scraped_data': scraped_data})
