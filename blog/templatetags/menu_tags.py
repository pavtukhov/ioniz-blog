from django import template
register = template.Library()
  
"""
@register.inclusion_tag('blog/menu.html')
def show_menu(blog):
    menu = get_template('blog/menu.html')
    return {'menu': menu}

@register.inclusion_tag('collection/block_prizer.html')
def show_prizer(prizer):
    "Show prizer template in prizer list"
    return {'prizer': prizer}


def menu(request):
    menu = get_template('blog/menu.html')
    return menu.render()
	register.inclusion_tag('menu')

from django.template.loader import get_template
t = get_template('results.html')
register.inclusion_tag(t)(show_results)

"""
