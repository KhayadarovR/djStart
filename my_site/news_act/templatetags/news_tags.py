from django import template
from django.db.models import *
from news_act.models import Category
from django.core.cache import cache

register = template.Library()


@register.simple_tag(name='get_list_cat')
def get_categories():
    return Category.objects.all()


@register.inclusion_tag(filename='news_act/list_categories.html')
def show_categories():
    # categories = cache.get('categories')
    # if not categories:
    categories = Category.objects.annotate(cnt=Count('get_news')).filter(cnt__gt=0)
        # cache.set('categories', categories, 30)

    context = {
        'categories': categories
    }

    return context