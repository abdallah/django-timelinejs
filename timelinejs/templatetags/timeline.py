from django import template
from django.core.urlresolvers import reverse

register = template.Library()

@register.inclusion_tag('timeline_template.html', takes_context=True)
def timeline(context, src=None, **config):
    try:
        if src is None:
            src = context['timeline'].pk
        if isinstance(src, int):
            config['src'] = '%s?format=json' % reverse('timelineview', kwargs={'pk':src})
        elif src.isdigit():
            print 'its a digit ', src
            config['src'] = '%s?format=json' % reverse('timelineview', kwargs={'pk':src})
        else:
            config['src'] = src
        if context.has_key('options'):
            options = context['options']
            options.__dict__.update(config)
        else: 
            options = config
        return {'context': context, 'config': options}
    except Exception, e:
        raise e