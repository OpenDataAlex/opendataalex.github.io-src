#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Alex Meadows'
SITENAME = "OpenDataAlex's Blog"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'US/Eastern'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/OpenDataAlex'),
          ('LinkedIn', 'https://www.linkedin.com/in/alexmeadows/'),
          ('SllideShare', 'https://www.slideshare.net/dba_alex'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = "/home/ameadows/PycharmProjects/pelican-twitchy"

EXPAND_LATEST_ON_INDEX = True
OPEN_GRAPH = False
OPEN_GRAPH_IMAGE = False
SHARE = True

DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_TAGS_ON_MENU = True

CC_LICENSE = 'CC-BY-SA-ND-NC'

PLUGINS = [
    'minchin.pelican.plugins.cname'
]