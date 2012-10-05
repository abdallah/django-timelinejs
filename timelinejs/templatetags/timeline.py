from django import template
from django.core.urlresolvers import reverse

register = template.Library()

@register.inclusion_tag('timeline_template.html', takes_context=True)
def timeline(context, src=None, **config):
    if src is None:
        raise template.TemplateSyntaxError("timeline tag requires at least the src argument")
    if isinstance(src, int):
        config['src'] = '%s?format=json' % reverse('tlv', kwargs={'pk':src})
    elif src.isdigit():
        print 'its a digit ', src
        config['src'] = '%s?format=json' % reverse('tlv', kwargs={'pk':src})
    else:
        config['src'] = src
    options = context['options']
    options.__dict__.update(config)
    #return {'context': context, 'config': config}
    return {'context': context, 'config': options}