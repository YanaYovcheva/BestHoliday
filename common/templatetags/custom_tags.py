from django import template

register = template.Library()

@register.filter
def get_full_destination(destination):
    return f'{destination.name}, {destination.country}'
