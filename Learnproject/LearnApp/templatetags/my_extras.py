from django import template

register = template.Library()

@register.filter(name = 'AddOn')
def AddOn(value):
    """this function add all number in string """
    f = str(value)  
    total = 0
    for i in f:
        total = total + int(i)

    return total
#register.filter('addon',AddOn)
