from django import template
from django.utils.safestring import mark_safe
from taggit.models import Tag
from ..models import Category
import markdown

register = template.Library()


# markdown filter
@register.filter(name='markdown_format')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))


# return all tags or a given number of tags
@register.inclusion_tag('summaries/summary/tags_list.html')
def tags_list(num=None):
    if num:
        tags_list = Tag.objects.all()[int(num)]
    else:
        tags_list = Tag.objects.all()
    return {'tags_list': tags_list}


# return all categories or a given number of category
@register.inclusion_tag('summaries/summary/category_list.html')
def category_list(num=None):
    if num:
        category_list = Category.objects.all()[int(num)]
    else:
        category_list = Category.objects.all()
    return {'category_list': category_list}


# return all categories or a given number of category
@register.inclusion_tag('summaries/summary/category_list_for_navbar.html')
def category_list_for_navbar(num=None):
    if num:
        category_list = Category.objects.all()[int(num)]
    else:
        category_list = Category.objects.all()
    return {'category_list': category_list}


