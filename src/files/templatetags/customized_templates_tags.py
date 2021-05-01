from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def real_name(value):
    """Show only the real name of the file"""
    split = value.split('/')
    _return = split[0]
    if len(split) > 1:
        _return = split[1]
    return _return
