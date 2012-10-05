from django.contrib.admin import site, ModelAdmin, StackedInline
from timelinejs.models import Timeline, TimelineEvent, TimelineOptions
from timeline.settings import STATIC_URL

class CommonMedia:
    js = (
      #'https://ajax.googleapis.com/ajax/libs/dojo/1.6.0/dojo/dojo.xd.js',
      #'admin/js/editor.js',
      'admin/js/inlinecollapsed.js',
    )
    css = {
      'all': ('admin/css/editor.css',),
    }
  
class OptionsInline(StackedInline):
    model = TimelineOptions
    
class EventsInline(StackedInline):
    model = TimelineEvent
    
class TimelineAdmin(ModelAdmin):
    fieldsets = (
        (None, {'fields': (('headline', 'start_date'), 'text')}), 
        ('Assets', {
            'classes': ('collapse',),
            'fields': ('asset_media', 'asset_credit', 'asset_caption')
        })
    )
    inlines = [OptionsInline, EventsInline]
    Media = CommonMedia


site.register(Timeline, TimelineAdmin)
site.register(TimelineEvent)
site.register(TimelineOptions)