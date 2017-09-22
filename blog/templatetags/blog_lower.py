from django import template
from django.template.defaultfilters import stringfilter

from django.utils.safestring import SafeData, mark_safe
from django.utils.text import (
    normalize_newlines, )

register = template.Library()


@register.filter('blog_lower', is_safe=True)
@stringfilter
def blog_lower(value):  # Only one argument.
    return value.lower()





# @register.filter("linebreaksbr", is_safe=True, needs_autoescape=True)
# @stringfilter
# def linebreaksbr(value, autoescape=True):
#     """
#     Converts all newlines in a piece of plain text to HTML line breaks
#     (``<br />``).
#     """
#     autoescape = autoescape and not isinstance(value, SafeData)
#     value = normalize_newlines(value)
#     if autoescape:
#         value = escape(value)
#     return mark_safe(value.replace('\n', '<br />'))
