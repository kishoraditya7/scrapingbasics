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

