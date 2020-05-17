from django import template
from ..models import Category

register = template.Library()

@register.inclusion_tag('entries/base.html') # This does not work because of recursive calling .... :(
#@register.filter

def categories_list():
    categories = Category.objects.all()
    return {'categories': categories}
    #print('prosim ')
    #return {'categories': 'bla'}
