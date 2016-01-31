#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Stephen Haffner'
EMAIL = 'admin@kd8zev.net'
SITENAME = u'Stephen J. Haffner | kd8zev'
SITEURL = 'https://www.haffner.me'
RESUME = 'static/HaffnerStephen-Resume.pdf'

PATH = 'content'
STATIC_PATHS = ['images', 'static']
PLUGIN_PATHS = ['plugins']
PLUGINS = ['pin_to_top', 'pelican-page-hierarchy']

THEME = 'pelican-theme-zev'

DEFAULT_LANG = u'en'
TIMEZONE = 'America/New_York'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
#AUTHOR_FEED_ATOM = None
#AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),)

# Social widget
SOCIAL = (('GitHub', 'https://githut.com/yupyupp'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
