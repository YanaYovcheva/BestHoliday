from django import template

register = template.Library()

@register.filter
def get_full_destination(destination):
    return f'{destination.name}, {destination.country}'


@register.filter
def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists()
