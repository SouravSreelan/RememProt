from django import template

register = template.Library()

def modify_name(value):
    if '_' in value:
       value = value.replace('_','/')
    return value

register.filter('modify_name', modify_name)
