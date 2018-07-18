#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os

AUTHOR = 'Dr. Juan Camilo Orduz'
SITENAME = 'Dr. Juan Camilo Orduz'
SITEURL = 'http://juanitorduz.github.io'
#SITEIMAGE = 'images/glue.png width=500 height=220'

SITESUBTITLE = 'Mathematician & Data Scientist'



PYGMENTS_STYLE = 'default'

PATH = 'content'

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


MARKUP = ('md', 'Rmd', 'rmd',)


EXTRA_HEADER = open('_nb_header.html').read().decode('utf-8') if os.path.exists('_nb_header.html') else None


NOTEBOOK_DIR = 'notebooks'

# Blogroll
LINKS = (
    ('LinkedIn', 'https://www.linkedin.com/in/juanitorduz'),
    ('GitHub', 'https://github.com/juanitorduz'),
    #('You can modify those links in your config file', '#'),
    )


# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME="themes/pelican-alchemy/alchemy"
#THEME="themes/pelican-elegant"

PLUGIN_PATHS=['pelican-plugins']

PLUGINS = ['liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.youtube', 'liquid_tags.vimeo',
           'liquid_tags.include_code', 'liquid_tags.notebook',
           'liquid_tags.literal', 'render_math', 'latex']

STATIC_PATHS = ['notebooks', 'images', 'pages', 'documents', 'pdfs']

DELETE_OUTPUT_DIRECTORY = False
LOAD_CONTENT_CACHE = False

GOOGLE_ANALYTICS = "UA-122570825-1"


