from atexit import register
from django import template

from categories.models import Categories


register = template.Library()


@register.simple_tag()
def tag_categories():
    return Categories.objects.all()