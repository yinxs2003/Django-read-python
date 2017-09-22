from django import template

register = template.Library()

@register.filter("blog_debug")
def blog_debug(request):
    crash_here