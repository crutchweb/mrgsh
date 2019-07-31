from django.shortcuts import render
from django import template
from main.models import News, Category
from pprint import pprint

register = template.Library()


@register.inclusion_tag('include/widget_news.html')
def show_widget_news():
    items = News.objects.all()
    return {'items': items}


@register.inclusion_tag('include/categories.html')
def show_categories():
    items = Category.objects.all()    
    return {'items': items}