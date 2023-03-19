from django import template

register = template.Library()

@register.filter(name="custom_zip")
def custom_zip(a,b):
    return zip(a,b)