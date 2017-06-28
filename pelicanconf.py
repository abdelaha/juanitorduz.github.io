#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Juan Camilo Orduz'
SITENAME = 'Juan Camilo Orduz'
SITEURL = 'http://juanitorduz.github.io'

PATH = 'content'

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('LinkedIn', 'https://www.linkedin.com/in/juanitorduz'),
    #('You can modify those links in your config file', '#'),
    )

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME="themes/pelican-elegant"

PLUGIN_PATHS=['pelican-plugins','plugins']
PLUGINS=['liquid_tags.notebook', 'ipynb.liquid',]

STATIC=['notebooks']

EXTRA_HEADER = open('_nb_header.html').read().decode('utf-8')

DISQUS_SITENAME = "juanitorduz"

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.toc': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}



