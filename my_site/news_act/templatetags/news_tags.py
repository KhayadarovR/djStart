from django import template
from django.db.models import *
from news_act.models import Category


register = template.Library()


@register.simple_tag(name='get_list_cat')
def get_categories():
    return Category.objects.all()


@register.inclusion_tag(filename='news_act/list_categories.html')
def show_categories():
    categories = Category.objects.annotate(cnt=Count('get_news')).filter(cnt__gt=0)
    context = {
        'categories': categories
    }

    return context