# Django-TimelineJS 
## Document history with TimelineJS
Tags: timeline, shortcode, stamen, timeline.verite.co, VeriteCo, HTML5

Use TimelineJS developed by VéritéCo for your Django site. Just load the tags.
I'm simply going to copy and adapt the info and docs as per the [TimelineJS-Wordpress-Plugin](https://github.com/VeriteCo/TimelineJS-Wordpress-Plugin)

## Description

There are lots of timeline tools on the web but they are almost all either
hard on the eyes or hard to use. Create timelines that are at the same time
beautiful and intuitive for users

TimelineJS is great for pulling in media from different sources. Just throw in a
link from Twitter, YouTube, Flickr, Vimeo, Google Maps or SoundCloud and
TimelineJS will format it to fit perfectly. More media types will be supported
in the future.

You can use the django admin to add a timeline and populate it with events.
You can then embed the Timeline in your templates using this tag:
`{% load timeline %}{% timeline %}`

## Installation

1. pip install django-timelinejs
1. add 'timelinejs' to your INSTALLED_APPS and run ./manage.py syncdb
1. add the appropriate urls to your urls.py
1. create the timelines in admin
1. use the timelines in your templates

## Template Options

Here are some of the options you can set in the config.
The template tag will work as following:
```python
{% load timeline %}
{% timeline %} {# will pull the timeline from context['timeline'] if available #}
{% timeline 1 %} {# will pull timeline with pk=1 and load it in the template #}
{% timeline src='/some/link/to/source/json' %} {# will pull the timeline from a json source #}
```

You can also add the options below:
```python
{% timeline src='1' lang='fr' debug=True font='Rancho-Gudea' %}
```

Here's more information on the options.

### Language
`lang`
Localization
*default is en*
Languages available:
* `en` *English*
* `fr` *Français*
* `es` *Español*
* `de` *Deutsch*
* `it` *Italiano*
* `pt-br` *Português Brazil*
* `pt` *Português*
* `nl` *Dutch*
* `cz` *Czech*
* `dk` *Danish*
* `no` *Norwegian*
* `id` *Indonesian*
* `pl` *Polish*
* `sl` *Slovenian*
* `ru` *Russian*
* `sk` *Slovak*
* `is` *Icelandic*
* `fo` *Faroese*
* `kr` *월요일*
* `ja` *日本語*
* `zh-ch` *中文*
* `zh-tw` *Taiwanese Mandarin*
* `ta` *தமிழ் - Tamil*
* `ar` *Arabic* *May be issues with right to left (need some help here)* 

Help us add more. Grab a copy of a language file and replace it with your language [Example language file](https://github.com/VeriteCo/StoryJS-Core/blob/master/Language/locale/en.js) and find your language's [two letter code here](http://spreadsheets.google.com/pub?key=p9pdwsai2hDMsLkXsoM05KQ&gid=1)

###Start at End 
`start_at_end`
set to true to start the timeline on the last date.
*default is false*

###Start at Slide 
`start_at_slide`
You can tell TimelineJS to start at a specific slide number
*default is 0*

###Start Zoom Adjust
`start_zoom_adjust`
This will tweak the default zoom level. Equivilent to pressing the zoom in or zoom out button the specified number of times. Negative numbers zoom out.
*default is 0*

###Hash Bookmark 
`hash_bookmark`
set to true to allow bookmarking slides using the hash tag
*default is false*

###Debug 
`debug`
Will log events etc to the console.
*default is false*


###Map Style Types 
Due to recent changes to the Google Maps API, you need a [API Key](https://developers.google.com/places/documentation/#Authentication) in order to use custom map types.
`gmap_key:`
*required in order to use maptype*

`maptype:`
* [Stamen Maps ](maps.stamen.com)
* `toner`
* `toner-lines`
* `toner-labels`
* `watercolor`
* `sterrain`
		
* Google Maps
* `ROADMAP`
* `TERRAIN`
* `HYBRID`
* `SATELLITE`

###Font Options 
`font:`
* `Arvo-PTSans`
* `Merriweather-NewsCycle`
* `PoiretOne-Molengo`
* `PTSerif-PTSans`
* `DroidSerif-DroidSans`
* `Lekton-Molengo`
* `NixieOne-Ledger`
* `AbrilFatface-Average`
* `PlayfairDisplay-Muli`
* `Rancho-Gudea`
* `Bevan-PotanoSans`
* `BreeSerif-OpenSans`
* `SansitaOne-Kameron`
* `Pacifico-Arimo`
* Or make your own

####Font Combination Preview:
![Font Combination Preview](http://timeline.verite.co/gfx/font-options.png)
  
## Best practices

Tips and tricks to best utilize TimelineJS

  1. Keep it light - don’t get bogged down by text or other elements
  2. Pick stories that have a strong chronological narrative. It does not work well for stories that need to jump around in the timeline.
  3. Include events that build up to major occurrences, not just the major events.
  4. Don't overwhelm the user. A timeline with hundreds of events is probably not the best use of the format.
  
## License
This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.

## Changelog

### 0.2 ###
* First stable release.

