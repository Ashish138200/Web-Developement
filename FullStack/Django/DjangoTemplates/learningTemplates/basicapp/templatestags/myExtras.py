# Creating custom filters
from django import template

register = template.Library()

@register.filter(name=cut) #decorators
def cut(value,arg):
    """
    This cuts out all value of "arg" from the string!
    :param value:
    :param arg:
    :return:
    """
    return value.replace(arg,'')
#register.filter('cut',cut)