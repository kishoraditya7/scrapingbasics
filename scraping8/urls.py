"""
URL configuration for scraping8 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
"""from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]"""
from django.urls import path
from functionsbase.views import (
    index, 
    results, 
    robots_txt, 
    html_code, 
    html_code_parser,
    parse_tree, 
    classes, 
    elements, 
    tags, 
    attributes, 
    scrape_with_class, 
    scrape_with_class_group, 
    scrape_with_attribute,
    scrape_with_element, 
    scrape_with_tag, 
    scrape_with_element_group,
    scrape_with_attribute_group,
    scrape_with_tag_group,
    html_requests,
    html_html_parser,
    html_lxml,
    html_lxml_xml,
    html_html5lib,
    tree_design,
    sitemap,
    demos,
    )


urlpatterns = [
    path('', index, name='index'),
    path('results/', results, name='results'),
    path('robots-txt/', robots_txt, name='robots_txt'),
    path('html-code/', html_code, name='html_code'),
    path('html-code/<str:parser>/', html_code_parser, name='html_code_parser'),
    path('parse-tree/', parse_tree, name='parse_tree'),
    path('classes/', classes, name='classes'),
    path('elements/', elements, name='elements'),
    path('tags/', tags, name='tags'),
    path('attributes/', attributes, name='attributes'),
    path('scrape-with-class/', scrape_with_class, name='scrape-with-class'),
    path('scrape-with-class-group/', scrape_with_class_group, name='scrape-with-class-group'),
    path('scrape_with_element/', scrape_with_element, name='scrape_with_element'),
    path('scrape_with_tag/', scrape_with_tag, name='scrape_with_tag'),
    path('scrape_with_attribute/', scrape_with_attribute, name='scrape_with_attribute'),
    path('scrape_with_element_group/', scrape_with_element_group, name='scrape_with_element_group'),
    path('scrape_with_attribute_group/', scrape_with_attribute_group, name='scrape_with_attribute_group'),
    path('scrape_with_tag_group/', scrape_with_tag_group, name='scrape_with_tag_group'),
    path('html_requests/', html_requests, name='html_requests'),
    path('html_html_parser/', html_html_parser, name='html_html_parser'),
    path('html_lxml/', html_lxml, name='html_lxml'),
    path('html_lxml_xml/', html_lxml_xml, name='html_lxml_xml'),
    path('html_html5lib/', html_html5lib, name='html_html5lib'),
    path('tree_design/', tree_design, name='tree_design'),
    path('sitemap/', sitemap, name='sitemap'),
    path('demos/', demos, name='demos'),
    ]



