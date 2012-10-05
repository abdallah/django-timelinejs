# coding: utf-8
from django.db import models
from django.utils import simplejson


class Timeline(models.Model):
    headline = models.CharField(max_length=200, help_text='Headline for timeline')
    type = models.CharField(max_length=50, default="default")
    start_date = models.DateField(blank=True, help_text='Timeline start date')
    text = models.TextField(blank=True, help_text='Description of timeline')
    asset_media = models.CharField(max_length=200, blank=True, verbose_name='media', help_text='Media to add to even info: Picutre link, YouTube, Wikipedia, etc.')
    asset_credit = models.CharField(max_length=200, blank=True, verbose_name='credit', help_text='Media credits here')
    asset_caption = models.CharField(max_length=200, blank=True, verbose_name='caption', help_text='Caption for media')
    
    def to_dict(self):
        d = {}
        d['startDate'] = self.start_date.strftime('%Y,%m,%d')
        d['type'] = self.type
        d['headline'] = self.headline
        d['text'] = self.text
        d['asset'] = {'media': self.asset_media, 'credit': self.asset_credit, 'caption': self.asset_caption }
        events = []
        for e in self.timelineevent_set.all():
            events.append(dict([(attr, str(getattr(e, attr))) for attr in [f.name for f in e._meta.fields]]))
        d['date'] = [ e.to_dict() for e in self.timelineevent_set.all()]
        timeline = {'timeline': d}
        return timeline
    
    def __str__(self):
        return "%s - %s" % (self.start_date, self.headline)

class TimelineEvent(models.Model):
    timeline = models.ForeignKey(Timeline)
    start_date = models.DateField(help_text='Event start date')
    end_date = models.DateField(blank=True, help_text='Event end date')
    headline = models.CharField(max_length=200, blank=True, help_text='Headline for event')
    text = models.TextField(blank=True, help_text='Text description of event')
    asset_media = models.CharField(max_length=200, blank=True, verbose_name='media', help_text='Media to add to even info: Picutre link, YouTube, Wikipedia, etc.')
    asset_credit = models.CharField(max_length=200, blank=True, verbose_name='credit', help_text='Media credits here')
    asset_caption = models.CharField(max_length=200, blank=True, verbose_name='caption', help_text='Caption for media')
    
    def to_dict(self):
        d = {}
        d['startDate'] = self.start_date.strftime('%Y,%m,%d')
        d['endDate'] = self.end_date.strftime('%Y,%m,%d')
        d['headline'] = self.headline
        d['text'] = self.text
        d['asset'] = {'media': self.asset_media, 'credit': self.asset_credit, 'caption': self.asset_caption }
        return d
    
    def __str__(self):
        return "%s - %s %s" % (self.start_date, self.end_date, self.headline)

class TimelineOptions(models.Model):
    FONT_CHOICES = (
            ('Arvo-PTSans', 'Arvo-PTSans'),
            ('Merriweather-NewsCycle', 'Merriweather-NewsCycle'),
            ('PoiretOne-Molengo', 'PoiretOne-Molengo'), 
            ('PTSerif-PTSans', 'PTSerif-PTSans'),
            ('DroidSerif-DroidSans', 'DroidSerif-DroidSans'),
            ('Lekton-Molengo', 'Lekton-Molengo'),
            ('NixieOne-Ledger', 'NixieOne-Ledger'),
            ('AbrilFatface-Average', 'AbrilFatface-Average'),
            ('PlayfairDisplay-Muli', 'PlayfairDisplay-Muli'),
            ('Rancho-Gudea', 'Rancho-Gudea'),
            ('Bevan-PotanoSans', 'Bevan-PotanoSans'),
            ('BreeSerif-OpenSans', 'BreeSerif-OpenSans'),
            ('SansitaOne-Kameron', 'SansitaOne-Kameron'),
            ('Pacifico-Arimo', 'Pacifico-Arimo')
        )
    LANG_CHOICES = (
            ('en', u'English'),
            ('fr', u'Français'),
            ('es', u'Español'),
            ('de', u'Deutsch'),
            ('it', u'Italiano'),
            ('pt-br', u'Português Brazil'),
            ('pt', u'Português'),
            ('nl', u'Dutch'),
            ('cz', u'Czech'),
            ('dk', u'Danish'),
            ('id', u'Indonesian'),
            ('pl', u'Polish'),
            ('sl', u'Slovenian'),
            ('ru', u'Russian'),
            ('sk', u'Slovak'),
            ('is', u'Icelandic'),
            ('fo', u'Faroese'),
            ('kr', u'월요일'),
            ('ja', u'日本語'),
            ('zh-ch', u'中文'),
            ('zh-tw', u'Taiwanese Mandarin'),
            ('ta', u'தமிழ் - Tamil'),
            ('ar', u'Arabic')
        )
    MAP_CHOICES = (
            ('Stamen Maps', 'Stamen Maps'),
            ('toner', 'toner'),
            ('toner-lines', 'toner-lines'),
            ('toner-labels', 'toner-labels'),
            ('watercolor', 'watercolor'),
            ('sterrain', 'sterrain'),
            ('Google Maps', 'Google Maps'),
            ('ROADMAP', 'ROADMAP'),
            ('TERRAIN', 'TERRAIN'),
            ('HYBRID', 'HYBRID'),
            ('SATELLITE', 'SATELLITE')
        )
    timeline = models.OneToOneField(Timeline, primary_key=True)
    width = models.CharField(max_length=10, default='100%',
                help_text='Width of timeline DIV')
    height = models.CharField(max_length=10, default='600',
                help_text='Height of timeline DIV')
    embed_id = models.CharField(max_length=20, blank=True, 
                help_text='ID of timeline DIV')
    start_at_end = models.BooleanField(default=False, 
                help_text='Set to true to start the timeline on the last date. default is false')
    start_at_slide = models.IntegerField(default=0,
                help_text='You can tell TimelineJS to start at a specific slide number default is 0')
    start_zoom_adjust = models.IntegerField(default=0,
                help_text='This will tweak the default zoom level. Equivalent to pressing the zoom in or zoom out button the specified number of times. Negative numbers zoom out. default is 0')
    hash_bookmark = models.BooleanField(default=False, 
                help_text='set to true to allow bookmarking slides using the hash tag default is false')
    font = models.CharField(max_length=50, choices=FONT_CHOICES, default='Bevan-PotanoSans',
                help_text='Font combination options')
    debug = models.BooleanField(default=False,
                help_text='Will log events etc to the console. default is false')
    lang = models.CharField(max_length=6, choices=LANG_CHOICES, default='en',
                help_text='Localization options. default is English')
    maptype = models.CharField(max_length=50, choices=MAP_CHOICES, default='watercolor', 
                help_text='google maps api needed [todo]')
      
    class Meta:
        verbose_name_plural = 'Timeline Options'
    
#'''JSON Format
#{
#    "timeline":
#    {
#        "headline":"The Main Timeline Headline Goes here",
#        "type":"default",
#        "startDate":"1888",
#        "text":"<p>Intro body text goes here, some HTML is ok</p>",
#        "asset":
#        {
#            "media":"http://yourdomain_or_socialmedialink_goes_here.jpg",
#            "credit":"Credit Name Goes Here",
#            "caption":"Caption text goes here"
#        },
#        "date": [
#            {
#                "startDate":"2011,12,10",
#                "endDate":"2011,12,11",
#                "headline":"Headline Goes Here",
#                "text":"<p>Body text goes here, some HTML is OK</p>",
#                "asset":
#                {
#                    "media":"http://twitter.com/ArjunaSoriano/status/164181156147900416",
#                    "credit":"Credit Name Goes Here",
#                    "caption":"Caption text goes here"
#                }
#            }
#        ]
#    }
#}
#'''