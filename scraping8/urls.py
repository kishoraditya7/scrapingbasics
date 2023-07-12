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
from functionsbase.views import index, results, robots_txt, html_code, html_code_parser,parse_tree, classes, elements, tags, attributes, scrape_with_class, scrape_with_class_group

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
    ]



