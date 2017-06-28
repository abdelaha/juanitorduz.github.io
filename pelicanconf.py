#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os

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

THEME="themes/pelican-bootstrap3"

PLUGIN_PATHS=['pelican-plugins','plugins']
PLUGINS = ['summary', 'liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.include_code', 'liquid_tags.notebook',
           'liquid_tags.literal', 'ipynb.liquid']

STATIC=['notebooks']



