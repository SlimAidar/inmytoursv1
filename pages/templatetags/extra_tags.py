from django import template

register = template.Library()


@register.filter
def times(args, number):
    return range(int(number))