from django import template
from django.template.defaultfilters import stringfilter
from django.utils.html import (
    normalize_newlines,escape
)
from django.utils.safestring import SafeData, mark_safe
import logging
register = template.Library()


@register.filter("blog_linebreaksbr", is_safe=True, needs_autoescape=True)
@stringfilter
def blog_linebreaksbr(value, autoescape=True):
    """
    Converts all newlines in a piece of plain text to HTML line breaks
    (``<br />``).
    """
    autoescape = autoescape and not isinstance(value, SafeData)
    value = normalize_newlines(value)
    if autoescape:
        value = escape(value)
    # value = value.replace('\n', '<br />')
    value = mark_safe(value.replace('\\n', '<br/>'))
    print(value)
    return value
